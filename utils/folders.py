"""Utility functions for HeyGen folders."""

from typing import List
from ..rest_client import HeyGenRESTClient
from ..schemas.folders import Folder, FolderCreateRequest, FolderUpdateRequest

async def create_folder(client: HeyGenRESTClient, req: FolderCreateRequest) -> Folder:
    pass

async def update_folder(client: HeyGenRESTClient, folder_id: str, req: FolderUpdateRequest) -> Folder:
    pass

async def list_folders(client: HeyGenRESTClient) -> List[Folder]:
    pass
