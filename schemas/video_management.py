"""Pydantic schemas for HeyGen video management."""

from pydantic import BaseModel
from typing import List

class Video(BaseModel):
    pass

class VideoListResponse(BaseModel):
    pass

class DeleteResponse(BaseModel):
    pass
