from __future__ import annotations

from .schemas import WebhookEndpointDeleteResponse
from .._http import api_request


async def delete_webhook_endpoint(
    *,
    endpoint_id: str,
) -> WebhookEndpointDeleteResponse:
    """Delete a webhook endpoint (DELETE /v1/webhook/endpoint.delete)."""
    params = {"endpoint_id": endpoint_id}
    return await api_request(
        "DELETE",
        "/v1/webhook/endpoint.delete",
        WebhookEndpointDeleteResponse,
        params=params,
    )
