"""Utility functions for HeyGen video management."""

from typing import List
from ..rest_client import HeyGenRESTClient
from ..schemas.video_management import Video, VideoListResponse

async def list_videos(client: HeyGenRESTClient) -> List[Video]:
    pass

async def get_video(client: HeyGenRESTClient, video_id: str) -> Video:
    pass

async def delete_video(client: HeyGenRESTClient, video_id: str) -> bool:
    pass
