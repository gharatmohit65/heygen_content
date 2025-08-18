from __future__ import annotations

from .schemas import GroupAvatarsResponse
from .._http import api_request


async def list_avatars_in_group(group_id: str) -> GroupAvatarsResponse:
    """List avatars in a group (v2/avatar_group/{group_id}/avatars)."""
    return await api_request("GET", f"/v2/avatar_group/{group_id}/avatars", GroupAvatarsResponse)
