from __future__ import annotations

from .schemas import WebhookEndpointsListResponse
from .._http import api_request


async def list_webhook_endpoints() -> WebhookEndpointsListResponse:
    """List all registered webhook endpoints (GET /v1/webhook/endpoint.list)."""
    return await api_request(
        "GET",
        "/v1/webhook/endpoint.list",
        WebhookEndpointsListResponse,
    )
