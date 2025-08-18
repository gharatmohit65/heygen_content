from __future__ import annotations

from .schemas import VideoStatusResponse
from .._http import api_request


async def get_video_status(video_id: str) -> VideoStatusResponse:
    """Retrieve status/details for a specific video (v1/video_status.get)."""
    return await api_request("GET", "/v1/video_status.get", VideoStatusResponse, params={"video_id": video_id})
