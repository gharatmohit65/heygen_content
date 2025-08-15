"""Tests for the HeyGen avatars utility functions."""

import pytest
from unittest.mock import AsyncMock

from ...schemas.avatars import Avatar, AvatarListResponse
from ...utils.avatars import list_avatars

@pytest.mark.asyncio
async def test_list_avatars():
    """Test the list_avatars function."""
    mock_client = AsyncMock()
    mock_avatars_data = [
        {
            "avatar_id": "avatar-123",
            "name": "Test Avatar",
        }
    ]
    mock_response = AvatarListResponse(data=[Avatar.model_validate(v) for v in mock_avatars_data])
    mock_client._request = AsyncMock(return_value=mock_response)

    avatars = await list_avatars(mock_client)

    assert len(avatars) == 1
    assert avatars[0].avatar_id == "avatar-123"
    mock_client._request.assert_called_once_with(
        method="GET",
        endpoint="/v2/avatars",
        response_model=AvatarListResponse,
    )
