"""Pydantic schemas for HeyGen webhooks."""

from pydantic import BaseModel
from typing import List

class Webhook(BaseModel):
    pass

class WebhookCreateRequest(BaseModel):
    pass

class WebhookListResponse(BaseModel):
    pass
