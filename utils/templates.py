"""Utility functions for HeyGen templates."""

from typing import List
from ..rest_client import HeyGenRESTClient
from ..schemas.templates import Template, RenderTemplateRequest, RenderTemplateResponse

async def list_templates(client: HeyGenRESTClient) -> List[Template]:
    pass

async def render_template(client: HeyGenRESTClient, req: RenderTemplateRequest) -> RenderTemplateResponse:
    pass
