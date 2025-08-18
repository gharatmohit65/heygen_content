from __future__ import annotations

from .schemas import FolderActionResponse
from .._http import api_request


async def restore_folder(folder_id: str) -> FolderActionResponse:
    """Restore a folder (POST /v1/folders/{folder_id}/restore)."""
    return await api_request(
        "POST",
        f"/v1/folders/{folder_id}/restore",
        FolderActionResponse,
    )
