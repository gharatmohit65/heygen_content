from __future__ import annotations

from typing import Any, TypeVar

import httpx
from pydantic import BaseModel

from ..config import config as heygen_config
from ..api.streaming._exceptions import (
    AuthenticationError,
    HeyGenAPIError,
    HeyGenValidationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    PermissionDeniedError,
    QuotaLimitError,
    CreditNotEnoughError,
)

T = TypeVar("T", bound=BaseModel)


def _normalize_base_url(raw: str) -> str:
    base = raw.rstrip("/")
    return base


async def api_request(
    method: str,
    path: str,
    response_model: type[T],
    *,
    params: dict | None = None,
    json: dict | None = None,
) -> T:
    """Perform an HTTP request to HeyGen with unified auth and error mapping."""
    base_url = _normalize_base_url(heygen_config.BASE_URL)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Api-Key": heygen_config.API_KEY,
    }

    async with httpx.AsyncClient(base_url=base_url, timeout=heygen_config.TIMEOUT, headers=headers) as client:
        try:
            resp = await client.request(method, path, params=params, json=json)

            if 200 <= resp.status_code < 300:
                try:
                    data = resp.json()
                    return response_model.model_validate(data)
                except Exception as e:
                    raise HeyGenValidationError(f"Invalid response: {e}") from e

            try:
                payload = resp.json() or {}
            except Exception:
                payload = {}

            code = payload.get("code")
            message = payload.get("message") or resp.text or "HeyGen API error"

            if resp.status_code == 401 or code in {40009, 400112, 401057, 401056}:
                raise AuthenticationError(message or "Invalid API key")

            if resp.status_code == 403 or code in {400573, 400562, 400578}:
                raise PermissionDeniedError(message or "Access forbidden")

            if resp.status_code == 404 or code in {40051, 400179, 400114, 404003, 404001, 400174, 400144}:
                raise NotFoundError(message or "Resource not found")

            if resp.status_code == 429 or code in {400140, 10007, 10015}:
                raise RateLimitError(message or "Rate limit exceeded")
            if code in {401029, 40019}:
                raise QuotaLimitError(message or "Quota limit reached")

            if code in {400118}:
                raise CreditNotEnoughError(message or "Insufficient credits")

            if resp.status_code == 400 or code in {
                40001,
                400175,
                40012,
                40065,
                40039,
                400105,
                40010,
                40031,
                40044,
                40072,
            }:
                raise HeyGenValidationError(message or "Invalid request data", details=payload)

            if 500 <= resp.status_code < 600 or code in {500000}:
                raise ServerError(message or "Internal server error")

            raise HeyGenAPIError(message or "HeyGen API error", status_code=resp.status_code, details=payload)

        except httpx.HTTPStatusError as e:
            raise HeyGenAPIError(
                f"HTTP error: {e.response.text}", status_code=e.response.status_code
            ) from e
        except httpx.RequestError as e:
            raise HeyGenAPIError(f"Request failed: {e}") from e
