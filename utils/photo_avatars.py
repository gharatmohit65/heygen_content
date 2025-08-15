"""Utility functions for HeyGen photo avatars."""

from ..rest_client import HeyGenRESTClient
from ..schemas.photo_avatars import PhotoAvatarCreateRequest, PhotoAvatarCreateResponse, PhotoAvatarStatus

async def create_photo_avatar(client: HeyGenRESTClient, req: PhotoAvatarCreateRequest) -> PhotoAvatarCreateResponse:
    pass

async def get_photo_avatar_status(client: HeyGenRESTClient, task_id: str) -> PhotoAvatarStatus:
    pass
