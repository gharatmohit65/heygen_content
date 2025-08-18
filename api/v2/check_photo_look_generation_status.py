from __future__ import annotations

from .schemas import PhotoAvatarGenerationStatusResponse
from .._http import api_request


async def check_photo_look_generation_status(
    generation_id: str,
) -> PhotoAvatarGenerationStatusResponse:
    """Check photo/look generation status (GET /v2/photo_avatar/generation/{generation_id})."""
    return await api_request(
        "GET",
        f"/v2/photo_avatar/generation/{generation_id}",
        PhotoAvatarGenerationStatusResponse,
    )
