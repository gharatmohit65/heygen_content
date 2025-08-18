from __future__ import annotations

from .schemas import VoicesResponse
from .._http import api_request


async def list_voices() -> VoicesResponse:
    """List voices (v2/voices)."""
    return await api_request("GET", "/v2/voices", VoicesResponse)
