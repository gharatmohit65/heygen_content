from __future__ import annotations

from .schemas import RemainingQuotaResponse
from .._http import api_request


async def get_remaining_quota() -> RemainingQuotaResponse:
    """Get remaining API quota (GET /v2/user/remaining_quota)."""
    return await api_request(
        "GET",
        "/v2/user/remaining_quota",
        RemainingQuotaResponse,
    )
