"""Asynchronous client for the HeyGen REST API."""

import httpx
from typing import Type, TypeVar, Optional
from pydantic import BaseModel, ValidationError as PydanticValidationError

from .config import config
from .api._exceptions import (
    HeyGenAPIError,
    AuthenticationError,
    HeyGenValidationError,
)

T = TypeVar("T", bound=BaseModel)

class HeyGenRESTClient:
    """Asynchronous client for HeyGen REST API."""

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None, timeout: Optional[int] = None):
        self.api_key = api_key or config.API_KEY
        self.base_url = base_url or config.BASE_URL
        self.timeout = timeout or config.TIMEOUT
        
        if not self.api_key:
            raise AuthenticationError("API key is not set.")

        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Api-Key": self.api_key,
            },
            timeout=self.timeout,
        )

    async def close(self):
        """Close the async client."""
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def _request(
        self,
        method: str,
        endpoint: str,
        response_model: Type[T],
        **kwargs,
    ) -> T:
        """
        Makes an async HTTP request and handles responses.

        Args:
            method: HTTP method (e.g., 'GET', 'POST').
            endpoint: API endpoint path.
            response_model: Pydantic model to validate the response.
            **kwargs: Additional arguments for httpx.request.

        Returns:
            A Pydantic model instance of the response.

        Raises:
            AuthenticationError: If the API key is invalid (401).
            HeyGenAPIError: For other non-2xx responses.
            HeyGenValidationError: If response JSON is invalid.
        """
        try:
            response = await self._client.request(method, endpoint, **kwargs)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise AuthenticationError("Authentication failed. Check your API key.") from e
            raise HeyGenAPIError(
                message=f"HeyGen API request failed: {e.response.text}",
                status_code=e.response.status_code
            ) from e

        try:
            return response_model.model_validate(response.json())
        except PydanticValidationError as e:
            raise HeyGenValidationError("Failed to validate response from HeyGen API.", details=e.errors()) from e
