from __future__ import annotations

from typing import Optional

from .schemas import BrandVoiceListResponse
from .._http import api_request


async def list_brand_voices(
    *,
    limit: Optional[int] = None,
    token: Optional[str] = None,
    name_only: Optional[bool] = None,
) -> BrandVoiceListResponse:
    """List brand voices (GET /v1/brand_voice/list).

    Params:
        limit: Defaults to 100
        token: Pagination token
        name_only: If true, only return names
    """
    params: dict[str, object] = {}
    if limit is not None:
        params["limit"] = limit
    if token is not None:
        params["token"] = token
    if name_only is not None:
        params["name_only"] = str(name_only).lower()

    return await api_request(
        "GET",
        "/v1/brand_voice/list",
        BrandVoiceListResponse,
        params=params or None,
    )
