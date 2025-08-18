from __future__ import annotations

from .schemas import CurrentUserInfoResponse
from .._http import api_request


async def get_current_user_info() -> CurrentUserInfoResponse:
    """Get current user information (GET /v1/user/me)."""
    return await api_request(
        "GET",
        "/v1/user/me",
        CurrentUserInfoResponse,
    )
