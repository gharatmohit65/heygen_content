"""Utility functions for HeyGen webhooks."""

from typing import List
from ..rest_client import HeyGenRESTClient
from ..schemas.webhooks import Webhook, WebhookCreateRequest

async def create_webhook(client: HeyGenRESTClient, req: WebhookCreateRequest) -> Webhook:
    pass

async def list_webhooks(client: HeyGenRESTClient) -> List[Webhook]:
    pass
