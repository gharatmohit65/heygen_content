"""Pydantic schemas for HeyGen folders."""

from pydantic import BaseModel
from typing import List

class Folder(BaseModel):
    pass

class FolderCreateRequest(BaseModel):
    pass

class FolderUpdateRequest(BaseModel):
    pass

class FolderListResponse(BaseModel):
    pass
