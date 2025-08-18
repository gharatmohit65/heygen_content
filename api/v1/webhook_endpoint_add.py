from __future__ import annotations

from typing import Optional, List

from .schemas import WebhookEndpointAddResponse
from .._http import api_request


async def add_webhook_endpoint(
    *,
    url: str,
    events: Optional[List[str]] = None,
    entity_id: Optional[str] = None,
) -> WebhookEndpointAddResponse:
    """Add a webhook endpoint (POST /v1/webhook/endpoint.add)."""
    payload: dict[str, object] = {"url": url}
    if events is not None:
        payload["events"] = events
    if entity_id is not None:
        payload["entity_id"] = entity_id

    return await api_request(
        "POST",
        "/v1/webhook/endpoint.add",
        WebhookEndpointAddResponse,
        json=payload,
    )
