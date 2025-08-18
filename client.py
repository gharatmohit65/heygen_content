"""Thin async client for HeyGen Content API (v1 + v2)."""

from __future__ import annotations

from typing import Any, TypeVar

from pydantic import BaseModel

from .api._http import api_request

T = TypeVar("T", bound=BaseModel)


class HeyGenContentClient:
    """Minimal content client that proxies to the shared HTTP helper.

    Prefer using per-route utilities in `api/v1` and `api/v2`. Use this client
    for ad-hoc endpoints or when a helper isn't available yet.
    """

    async def request(
        self,
        method: str,
        path: str,
        response_model: type[T],
        *,
        params: dict | None = None,
        json: dict | None = None,
    ) -> T:
        return await api_request(method, path, response_model, params=params, json=json)


# Singleton instance
client = HeyGenContentClient()