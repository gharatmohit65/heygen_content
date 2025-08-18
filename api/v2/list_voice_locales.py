from __future__ import annotations

from .schemas import LocalesResponse
from .._http import api_request


async def list_voice_locales() -> LocalesResponse:
    """List voice locales (v2/voices/locales)."""
    return await api_request("GET", "/v2/voices/locales", LocalesResponse)
