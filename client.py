"""Async client for HeyGen Streaming API."""

from __future__ import annotations

from typing import Any, TypeVar

import httpx
from pydantic import BaseModel

from .api.streaming._exceptions import (
    AuthenticationError,
    HeyGenAPIError,
    HeyGenValidationError,
    NotFoundError,
    RateLimitError,
    ServerError,
)
from .api.streaming.new_sessions import NewSessionRequest, NewSessionResponse
from .api.streaming.send_task import SendTaskRequest, TaskResponse
from .api.streaming.start_session import StartSessionRequest, StartSessionResponse
from .config import config as heygen_config

T = TypeVar('T', bound=BaseModel)

class HeyGenStreamingClient:
    """Async client for HeyGen Streaming API."""
    
    _instance = None
    _lock = None  # Not needed without rate limiting
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: int | None = None,
    ):
        """Initialize the HeyGen Streaming client.
        
        Args:
            api_key: Your HeyGen API key. If not provided, will use HEYGEN_API_KEY from config.
            base_url: Base URL for the HeyGen API. If not provided, will use HEYGEN_BASE_URL from config.
            timeout: Request timeout in seconds. If not provided, will use HEYGEN_TIMEOUT from config.
        """
        # Use provided values or fall back to config
        self.api_key = api_key or heygen_config.API_KEY
        self.base_url = (base_url or heygen_config.BASE_URL).rstrip("/")
        self.timeout = timeout or heygen_config.TIMEOUT
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> "HeyGenStreamingClient":
        """Async context manager entry."""
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        await self.close()

    async def start(self) -> None:
        """Initialize the HTTP client."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-Api-Key": self.api_key,
                },
            )

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None

    async def _request(
        self,
        method: str,
        endpoint: str,
        response_model: type[T],
        **kwargs: Any,
    ) -> T:
        """Send an HTTP request."""
        if not self._client:
            await self.start()

        try:
            response = await self._client.request(method, endpoint, **kwargs)

            # Fast-path for success
            if 200 <= response.status_code < 300:
                try:
                    data = response.json()
                    return response_model.model_validate(data)
                except Exception as e:
                    raise HeyGenValidationError(f"Invalid response: {e}") from e

            # Error path: map HeyGen errors to SDK exceptions
            error_payload = {}
            try:
                error_payload = response.json() or {}
            except Exception:
                # Non-JSON error body
                error_payload = {}

            code = error_payload.get("code")
            message = error_payload.get("message") or response.text or "HeyGen API error"

            # Authentication
            if response.status_code == 401 or code in {40009, 400112, 401057, 401056}:
                raise AuthenticationError(message or "Invalid API key")

            # Permission/Forbidden
            if response.status_code == 403 or code in {400573, 400562, 400578}:
                from .api.streaming._exceptions import PermissionDeniedError

                raise PermissionDeniedError(message or "Access forbidden")

            # Not found
            if response.status_code == 404 or code in {40051, 400179, 400114, 404003, 404001, 400174, 400144}:
                raise NotFoundError(message or "Resource not found")

            # Rate limiting / quota
            if response.status_code == 429 or code in {400140, 10007, 10015}:
                raise RateLimitError(message or "Rate limit exceeded")
            if code in {401029, 40019}:
                from .api.streaming._exceptions import QuotaLimitError

                raise QuotaLimitError(message or "Quota limit reached")

            # Credits
            if code in {400118}:
                from .api.streaming._exceptions import CreditNotEnoughError

                raise CreditNotEnoughError(message or "Insufficient credits")

            # Validation / bad request
            if response.status_code == 400 or code in {
                40001,
                400175,
                40012,
                40065,
                40039,
                400105,
                40010,
                40031,
                40044,
                40072,
            }:
                raise HeyGenValidationError(message or "Invalid request data", details=error_payload)

            # Server errors
            if 500 <= response.status_code < 600 or code in {500000}:
                raise ServerError(message or "Internal server error")

            # Fallback
            raise HeyGenAPIError(
                message or "HeyGen API error",
                status_code=response.status_code,
                details=error_payload,
            )

        except httpx.HTTPStatusError as e:
            # httpx already considered this an error; provide a readable message
            raise HeyGenAPIError(
                f"HTTP error: {e.response.text}",
                status_code=e.response.status_code,
            ) from e
        except httpx.RequestError as e:
            raise HeyGenAPIError(f"Request failed: {e}") from e

    async def create_session(
        self,
        request: NewSessionRequest,
    ) -> NewSessionResponse:
        """Create a new streaming session.
        
        Args:
            request: NewSessionRequest with session configuration
            
        Returns:
            NewSessionResponse with session details
        """
        return await self._request(
            "POST",
            "/streaming.new",
            NewSessionResponse,
            json=request.model_dump(exclude_none=True),
        )

    async def start_session(
        self,
        session_id: str,
    ) -> StartSessionResponse:
        """Start an existing streaming session.
        
        Args:
            session_id: The ID of the session to start
            
        Returns:
            StartSessionResponse with status of the operation
        """
        request = StartSessionRequest(session_id=session_id)
        return await self._request(
            "POST",
            "/streaming.start",
            StartSessionResponse,
            json=request.model_dump(exclude_none=True),
        )
        
    async def send_task(
        self,
        request: SendTaskRequest,
    ) -> TaskResponse:
        """Send a task to an existing streaming session.
        
        Args:
            request: SendTaskRequest with task details
            
        Returns:
            TaskResponse with task ID and duration
        """
        return await self._request(
            "POST",
            "/streaming.task",
            TaskResponse,
            json=request.model_dump(exclude_none=True),
        )

# Singleton instance
client = HeyGenStreamingClient()