from __future__ import annotations

from .schemas import VideoDeleteResponse
from .._http import api_request


async def delete_video(video_id: str) -> VideoDeleteResponse:
    """Delete an avatar video (v1/video.delete)."""
    return await api_request("DELETE", "/v1/video.delete", VideoDeleteResponse, params={"video_id": video_id})
