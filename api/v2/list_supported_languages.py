from __future__ import annotations

from .schemas import SupportedLanguagesResponse
from .._http import api_request


async def list_supported_languages() -> SupportedLanguagesResponse:
    """List supported target languages for Video Translate (GET /v2/video_translate/target_languages)."""
    return await api_request("GET", "/v2/video_translate/target_languages", SupportedLanguagesResponse)
