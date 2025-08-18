from __future__ import annotations

from .schemas import VideoShareRequest, VideoShareResponse
from .._http import api_request


async def share_video(payload: VideoShareRequest) -> VideoShareResponse:
    """Retrieve public share URL for a video (v1/video/share)."""
    return await api_request("POST", "/v1/video/share", VideoShareResponse, json=payload.model_dump(exclude_none=True))
