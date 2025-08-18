from __future__ import annotations

from .schemas import AvatarsResponse
from .._http import api_request


async def list_avatars() -> AvatarsResponse:
    """List avatars and talking photos (v2/avatars)."""
    return await api_request("GET", "/v2/avatars", AvatarsResponse)
