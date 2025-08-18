from __future__ import annotations

from .schemas import CreateFolderRequest, CreateFolderResponse
from .._http import api_request


async def create_folder(payload: CreateFolderRequest) -> CreateFolderResponse:
    """Create a folder (POST /v1/folders/create)."""
    return await api_request(
        "POST",
        "/v1/folders/create",
        CreateFolderResponse,
        json=payload.model_dump(exclude_none=True),
    )
