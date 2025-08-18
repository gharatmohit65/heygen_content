from __future__ import annotations

from .schemas import FolderActionResponse
from .._http import api_request


async def trash_folder(folder_id: str) -> FolderActionResponse:
    """Move a folder to trash (POST /v1/folders/{folder_id}/trash)."""
    return await api_request(
        "POST",
        f"/v1/folders/{folder_id}/trash",
        FolderActionResponse,
    )
