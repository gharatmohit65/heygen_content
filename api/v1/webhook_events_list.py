from __future__ import annotations

from .schemas import WebhookEventsListResponse
from .._http import api_request


async def list_available_webhook_events() -> WebhookEventsListResponse:
    """List all supported webhook events (GET /v1/webhook/webhook.list)."""
    return await api_request(
        "GET",
        "/v1/webhook/webhook.list",
        WebhookEventsListResponse,
    )
