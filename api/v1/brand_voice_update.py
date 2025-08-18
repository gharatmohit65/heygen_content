from __future__ import annotations

from .schemas import UpdateBrandVoiceRequest, UpdateBrandVoiceResponse
from .._http import api_request


async def update_brand_voice(
    brand_voice_id: str,
    payload: UpdateBrandVoiceRequest,
) -> UpdateBrandVoiceResponse:
    """Update an existing brand voice (POST /v1/brand_voice/{brand_voice_id})."""
    return await api_request(
        "POST",
        f"/v1/brand_voice/{brand_voice_id}",
        UpdateBrandVoiceResponse,
        json=payload.model_dump(exclude_none=True),
    )
