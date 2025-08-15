"""Utility functions for HeyGen video translation."""

from ..rest_client import HeyGenRESTClient
from ..schemas.translation import TranslateVideoRequest, TranslateVideoResponse, TranslationTask

async def translate_video(client: HeyGenRESTClient, req: TranslateVideoRequest) -> TranslateVideoResponse:
    pass

async def get_translation_status(client: HeyGenRESTClient, task_id: str) -> TranslationTask:
    pass
