"""Pydantic schemas for HeyGen assets."""

from pydantic import BaseModel
from typing import List

class Asset(BaseModel):
    pass

class AssetUploadResponse(BaseModel):
    pass

class AssetListResponse(BaseModel):
    pass
