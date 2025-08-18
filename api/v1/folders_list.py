from __future__ import annotations

from typing import Optional

from .schemas import ListFoldersResponse
from .._http import api_request


async def list_folders(
    *,
    limit: Optional[int] = None,
    parent_id: Optional[str] = None,
    name_filter: Optional[str] = None,
    is_trash: Optional[bool] = None,
    token: Optional[str] = None,
) -> ListFoldersResponse:
    """List folders (GET /v1/folders)."""
    params: dict[str, object] = {}
    if limit is not None:
        params["limit"] = limit
    if parent_id is not None:
        params["parent_id"] = parent_id
    if name_filter is not None:
        params["name_filter"] = name_filter
    if is_trash is not None:
        params["is_trash"] = str(is_trash).lower()
    if token is not None:
        params["token"] = token
    return await api_request(
        "GET",
        "/v1/folders",
        ListFoldersResponse,
        params=params or None,
    )
