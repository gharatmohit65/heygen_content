from __future__ import annotations

import types
import pytest

# Import API modules
from backend.app.core.third_party_integrations.heygen_content.api.v1 import (
    list_brand_voices,
    get_current_user_info,
    list_webhook_endpoints,
    list_folders,
    create_folder,
    update_folder,
    trash_folder,
    restore_folder,
)
from backend.app.core.third_party_integrations.heygen_content.api.v2 import (
    list_avatars,
    list_supported_languages,
    generate_photo_avatar_photos,
    check_photo_look_generation_status,
    get_remaining_quota,
)
from backend.app.core.third_party_integrations.heygen_content.api.v1.schemas import (
    CreateFolderRequest,
    UpdateFolderRequest,
)

# Module under test for HTTP layer
from backend.app.core.third_party_integrations.heygen_content.api import _http as http_mod


class FakeResponse:
    def __init__(self, status_code: int, json_payload: dict | list | None = None, text: str = "") -> None:
        self.status_code = status_code
        self._json = json_payload if json_payload is not None else {}
        self.text = text
        self.headers = {}

    def json(self):
        return self._json


class FakeAsyncClient:
    def __init__(self, *, base_url: str, timeout: int, headers: dict):
        self.base_url = base_url
        self.timeout = timeout
        self.headers = headers

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    async def request(self, method: str, path: str, params: dict | None = None, json: dict | None = None):
        # Route to canned responses based on path
        key = (method.upper(), path)
        # Minimal fakes for the endpoints we test
        if key == ("GET", "/v1/brand_voice/list"):
            return FakeResponse(200, {"code": 0, "data": {"voices": [{"id": "bv_1", "name": "Brand"}]}})
        if key == ("GET", "/v1/user/me"):
            return FakeResponse(200, {"code": 0, "data": {"username": "tester", "email": "t@example.com"}})
        if key == ("GET", "/v1/webhook/endpoint.list"):
            return FakeResponse(200, {"code": 0, "data": {"endpoints": []}})
        if key == ("GET", "/v1/folders"):
            return FakeResponse(200, {"code": 0, "data": {"folders": [{"id": "fld_1", "name": "root"}], "next_token": None}})
        if key == ("POST", "/v1/folders/create"):
            name = (json or {}).get("name", "")
            return FakeResponse(200, {"code": 0, "data": {"id": "fld_new", "name": name}})
        if path.startswith("/v1/folders/") and method.upper() == "POST" and path.count("/") == 3:
            # rename: /v1/folders/{folder_id}
            folder_id = path.split("/")[-1]
            return FakeResponse(200, {"code": 0, "data": {"id": folder_id, "name": (json or {}).get("name", "renamed")}})
        if path.endswith("/trash") and method.upper() == "POST":
            folder_id = path.split("/")[-2]
            return FakeResponse(200, {"code": 0, "data": {"id": folder_id, "trashed": True}})
        if path.endswith("/restore") and method.upper() == "POST":
            folder_id = path.split("/")[-2]
            return FakeResponse(200, {"code": 0, "data": {"id": folder_id, "trashed": False}})
        if key == ("GET", "/v2/avatars") or key == ("GET", "/v2/avatar"):
            # depending on actual implementation path; our util uses list_avatars -> v2 list endpoint
            return FakeResponse(200, {"data": {"avatars": []}})
        if key == ("GET", "/v2/video_translate/target_languages"):
            return FakeResponse(200, {"languages": ["en", "es"]})
        if key == ("POST", "/v2/photo_avatar/photo/generate"):
            return FakeResponse(200, {"generation_id": "gen_123"})
        if path.startswith("/v2/photo_avatar/generation/") and method.upper() == "GET":
            return FakeResponse(200, {"status": "completed", "image_keys": ["img_1"]})
        if key == ("GET", "/v2/user/remaining_quota"):
            return FakeResponse(200, {"remaining_quota": 120, "details": {"interactive": 60}})

        return FakeResponse(404, {"message": f"Unhandled route {method} {path}"}, text="not found")


@pytest.fixture(autouse=True)
def patch_http_and_config(monkeypatch):
    # Patch httpx.AsyncClient used by api/_http.py
    monkeypatch.setattr(http_mod, "httpx", types.SimpleNamespace(AsyncClient=FakeAsyncClient))

    # Patch config used by api/_http.py
    class Cfg:
        API_KEY = "test_key"
        BASE_URL = "https://api.heygen.com/v1"
        TIMEOUT = 10

    monkeypatch.setattr(http_mod, "heygen_config", Cfg())


@pytest.mark.asyncio
async def test_v1_list_brand_voices():
    resp = await list_brand_voices(limit=10, name_only=True)
    assert resp is not None
    assert getattr(resp, "data", None) is not None


@pytest.mark.asyncio
async def test_v1_get_current_user_info():
    me = await get_current_user_info()
    assert me is not None
    assert me.data is not None
    assert me.data.username == "tester"


@pytest.mark.asyncio
async def test_v1_list_webhook_endpoints():
    resp = await list_webhook_endpoints()
    assert resp is not None
    assert getattr(resp, "data", None) is not None


@pytest.mark.asyncio
async def test_v2_list_supported_languages():
    langs = await list_supported_languages()
    assert langs.languages == ["en", "es"]


@pytest.mark.asyncio
async def test_v2_generate_photo_avatar_and_check_status():
    gen = await generate_photo_avatar_photos(payload=type("P", (), {"model_dump": lambda self, exclude_none=True: {"name": "John"}})())
    assert gen.generation_id == "gen_123"
    status = await check_photo_look_generation_status("gen_123")
    assert getattr(status, "status", None) == "completed"


@pytest.mark.asyncio
async def test_v2_get_remaining_quota():
    q = await get_remaining_quota()
    assert q.remaining_quota == 120


@pytest.mark.asyncio
async def test_v1_folders_endpoints():
    # list
    listed = await list_folders(limit=10, name_filter="root")
    assert listed is not None and getattr(listed, "data", None) is not None
    # create
    created = await create_folder(CreateFolderRequest(name="test"))
    assert created.data is not None and created.data.get("id") == "fld_new"
    # update
    updated = await update_folder("fld_new", UpdateFolderRequest(name="renamed"))
    assert updated.data is not None and updated.data.get("name") == "renamed"
    # trash
    trashed = await trash_folder("fld_new")
    assert trashed.data is not None and trashed.data.get("trashed") is True
    # restore
    restored = await restore_folder("fld_new")
    assert restored.data is not None and restored.data.get("trashed") is False
