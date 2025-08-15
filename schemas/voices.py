"""Pydantic schemas for HeyGen voices."""

from pydantic import BaseModel, Field
from typing import List

class Voice(BaseModel):
    """Represents a single voice available in HeyGen."""
    voice_id: str = Field(..., description="The unique identifier for the voice.")
    name: str = Field(..., description="The name of the voice.")
    gender: str = Field(..., description="The gender of the voice (e.g., 'Male', 'Female').")
    language: str = Field(..., description="The language of the voice (e.g., 'en-US').")
    supported_styles: List[str] = Field(default_factory=list, description="A list of supported speaking styles.")

    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda x: x # No aliasing for now

class VoiceListResponse(BaseModel):
    """The response model for a list of voices."""
    data: List[Voice] = Field(..., description="A list of available voices.")
