"""Utility functions for HeyGen assets."""

from typing import List, Optional
from ..rest_client import HeyGenRESTClient
from ..schemas.assets import Asset, AssetUploadResponse

async def upload_asset(client: HeyGenRESTClient, file_bytes: bytes, filename: str, mime: str) -> AssetUploadResponse:
    pass

async def list_assets(client: HeyGenRESTClient, folder_id: Optional[str] = None) -> List[Asset]:
    pass
