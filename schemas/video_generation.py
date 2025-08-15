"""Pydantic schemas for HeyGen video generation."""

from pydantic import BaseModel

class GenerateVideoRequest(BaseModel):
    pass

class GenerateVideoResponse(BaseModel):
    pass

class VideoJob(BaseModel):
    pass
