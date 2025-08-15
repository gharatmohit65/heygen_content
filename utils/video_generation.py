"""Utility functions for HeyGen video generation."""

from ..rest_client import HeyGenRESTClient
from ..schemas.video_generation import GenerateVideoRequest, GenerateVideoResponse, VideoJob

async def generate_video(client: HeyGenRESTClient, req: GenerateVideoRequest) -> GenerateVideoResponse:
    pass

async def get_video_job(client: HeyGenRESTClient, job_id: str) -> VideoJob:
    pass
