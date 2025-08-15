"""Utility functions for interacting with the HeyGen avatars API."""

from typing import List
from ..rest_client import HeyGenRESTClient
from ..schemas.avatars import Avatar, AvatarListResponse

async def list_avatars(client: HeyGenRESTClient) -> List[Avatar]:
    """Retrieves a list of available avatars."""
    response = await client._request(
        method="GET",
        endpoint="/v2/avatars",
        response_model=AvatarListResponse,
    )
    return response.data
