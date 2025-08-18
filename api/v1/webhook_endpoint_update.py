from __future__ import annotations

from typing import Optional, List

from .schemas import WebhookEndpointUpdateResponse
from .._http import api_request


async def update_webhook_endpoint(
    *,
    endpoint_id: str,
    url: Optional[str] = None,
    events: Optional[List[str]] = None,
) -> WebhookEndpointUpdateResponse:
    """Update a webhook endpoint (PATCH /v1/webhook/endpoint.update)."""
    payload: dict[str, object] = {"endpoint_id": endpoint_id}
    if url is not None:
        payload["url"] = url
    if events is not None:
        payload["events"] = events

    return await api_request(
        "PATCH",
        "/v1/webhook/endpoint.update",
        WebhookEndpointUpdateResponse,
        json=payload,
    )
