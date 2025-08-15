"""Utility functions for interacting with the HeyGen voices API."""

from typing import List
from ..rest_client import HeyGenRESTClient
from ..schemas.voices import Voice, VoiceListResponse

async def list_voices(client: HeyGenRESTClient) -> List[Voice]:
    """Retrieves a list of available voices.

    Args:
        client: An instance of HeyGenRESTClient.

    Returns:
        A list of Voice objects.
    """
    response = await client._request(
        method="GET",
        endpoint="/v2/voices",
        response_model=VoiceListResponse,
    )
    return response.data
