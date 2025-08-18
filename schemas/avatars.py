"""Pydantic schemas for HeyGen avatars."""

from pydantic import BaseModel, Field
from typing import List

class Avatar(BaseModel):
    """Represents a single avatar available in HeyGen."""
    avatar_id: str = Field(..., description="The unique identifier for the avatar.")
    name: str = Field(..., description="The name of the avatar.")

class AvatarListResponse(BaseModel):
    """The response model for a list of avatars."""
    data: List[Avatar] = Field(..., description="A list of available avatars.")
