from __future__ import annotations

from .schemas import (
    GeneratePhotoAvatarPhotosRequest,
    GeneratePhotoAvatarPhotosResponse,
)
from .._http import api_request


async def generate_photo_avatar_photos(
    payload: GeneratePhotoAvatarPhotosRequest,
) -> GeneratePhotoAvatarPhotosResponse:
    """Generate photo avatar photos (POST /v2/photo_avatar/photo/generate)."""
    return await api_request(
        "POST",
        "/v2/photo_avatar/photo/generate",
        GeneratePhotoAvatarPhotosResponse,
        json=payload.model_dump(exclude_none=True),
    )
