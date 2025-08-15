"""Pydantic schemas for HeyGen templates."""

from pydantic import BaseModel
from typing import List

class Template(BaseModel):
    pass

class TemplateListResponse(BaseModel):
    pass

class RenderTemplateRequest(BaseModel):
    pass

class RenderTemplateResponse(BaseModel):
    pass
