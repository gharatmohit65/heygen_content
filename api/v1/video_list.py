from __future__ import annotations

from typing import Optional

from .schemas import VideoListResponse
from .._http import api_request


async def list_videos(
    limit: Optional[int] = None,
    folder_id: Optional[str] = None,
    title: Optional[str] = None,
    token: Optional[str] = None,
) -> VideoListResponse:
    """List videos (v1/video.list)."""
    params: dict = {}
    if limit is not None:
        params["limit"] = limit
    if folder_id:
        params["folder_id"] = folder_id
    if title:
        params["title"] = title
    if token:
        params["token"] = token
    return await api_request("GET", "/v1/video.list", VideoListResponse, params=params)
