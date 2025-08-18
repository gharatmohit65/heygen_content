from __future__ import annotations

from .schemas import CreateWebmRequest, CreateWebmResponse
from .._http import api_request


async def create_webm_video(payload: CreateWebmRequest) -> CreateWebmResponse:
    """Create a WebM video (v1/video.webm)."""
    return await api_request("POST", "/v1/video.webm", CreateWebmResponse, json=payload.model_dump(exclude_none=True))
