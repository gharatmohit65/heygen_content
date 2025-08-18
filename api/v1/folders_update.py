from __future__ import annotations

from .schemas import UpdateFolderRequest, UpdateFolderResponse
from .._http import api_request


async def update_folder(folder_id: str, payload: UpdateFolderRequest) -> UpdateFolderResponse:
    """Update folder name (POST /v1/folders/{folder_id})."""
    return await api_request(
        "POST",
        f"/v1/folders/{folder_id}",
        UpdateFolderResponse,
        json=payload.model_dump(exclude_none=True),
    )
