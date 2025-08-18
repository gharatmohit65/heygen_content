from __future__ import annotations

from .schemas import AvatarDetailsResponse
from .._http import api_request


async def get_avatar_details(avatar_id: str) -> AvatarDetailsResponse:
    """Retrieve avatar details (v2/avatar/{avatar_id}/details)."""
    return await api_request("GET", f"/v2/avatar/{avatar_id}/details", AvatarDetailsResponse)
