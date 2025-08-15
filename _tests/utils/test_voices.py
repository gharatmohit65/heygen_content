"""Tests for the HeyGen voices utility functions."""

import pytest
from unittest.mock import AsyncMock, patch

from ...schemas.voices import Voice, VoiceListResponse
from ...utils.voices import list_voices

@pytest.mark.asyncio
async def test_list_voices():
    """Test the list_voices function."""
    # Arrange
    mock_client = AsyncMock()
    mock_voices_data = [
        {
            "voice_id": "voice-123",
            "name": "Test Voice",
            "gender": "Female",
            "language": "en-US",
            "supported_styles": ["neutral"]
        }
    ]
    mock_response = VoiceListResponse(data=[Voice.model_validate(v) for v in mock_voices_data])
    
    # The mock for the client's _request method
    mock_client._request = AsyncMock(return_value=mock_response)

    # Act
    voices = await list_voices(mock_client)

    # Assert
    assert len(voices) == 1
    assert voices[0].voice_id == "voice-123"
    mock_client._request.assert_called_once_with(
        method="GET",
        endpoint="/v2/voices",
        response_model=VoiceListResponse,
    )
