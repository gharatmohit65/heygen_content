from __future__ import annotations

from typing import Optional

from .schemas import AvatarGroupsResponse
from .._http import api_request


async def list_avatar_groups(include_public: Optional[bool] = None) -> AvatarGroupsResponse:
    """List avatar groups (v2/avatar_group.list)."""
    params = {}
    if include_public is not None:
        params["include_public"] = str(include_public).lower()
    return await api_request("GET", "/v2/avatar_group.list", AvatarGroupsResponse, params=params)
