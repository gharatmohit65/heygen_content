from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field


# Common envelope for many v1 responses (code/message/msg)
class BaseEnvelope(BaseModel):
    code: Optional[int] = None
    message: Optional[str] = None
    msg: Optional[str] = None


# video_status.get
class VideoStatusData(BaseModel):
    callback_id: Optional[str] = None
    caption_url: Optional[str] = None
    created_at: Optional[float] = None
    duration: Optional[float] = None
    error: Optional[dict] = None
    gif_url: Optional[str] = None
    id: str
    status: Optional[str] = None  # processing|completed|failed|pending
    thumbnail_url: Optional[str] = None
    video_url: Optional[str] = None
    video_url_caption: Optional[str] = None


class VideoStatusResponse(BaseEnvelope):
    data: VideoStatusData


# video.delete
class VideoDeleteResponse(BaseEnvelope):
    data: Optional[dict] = None


# video.webm request/response
class Dimension(BaseModel):
    width: int
    height: int


class CreateWebmRequest(BaseModel):
    avatar_pose_id: Optional[str] = None
    avatar_style: Optional[str] = None  # circle|closeUp|normal|voiceOnly
    input_text: Optional[str] = None
    voice_id: Optional[str] = None
    input_audio: Optional[str] = None
    dimension: Optional[Dimension] = None


class CreateWebmData(BaseModel):
    video_id: str


class CreateWebmResponse(BaseEnvelope):
    data: CreateWebmData


# video.list
class VideoListItem(BaseModel):
    video_id: str
    status: Optional[str] = None
    created_at: Optional[float] = None
    type: Optional[str] = None  # GENERATED|TRANSLATED
    folder_id: Optional[str] = None
    title: Optional[str] = None


class VideoListData(BaseModel):
    token: Optional[str] = None
    total: Optional[int] = None
    videos: List[VideoListItem] = Field(default_factory=list)


class VideoListResponse(BaseEnvelope):
    data: VideoListData


# video.share
class VideoShareRequest(BaseModel):
    video_id: str


class VideoShareResponse(BaseEnvelope):
    data: Optional[dict] = None


# Brand Voice - list
class BrandVoiceListResponse(BaseEnvelope):
    # Unknown exact shape; allow passthrough
    data: Optional[dict] = None


# Brand Voice - update
class UpdateBrandVoiceRequest(BaseModel):
    name: Optional[str] = None
    blacklist: Optional[List[str]] = None
    whitelist: Optional[List[List[str]]] = None
    tones: Optional[List[str]] = None
    vocabulary: Optional[List[List[str]]] = None
    tone: Optional[str] = None


class UpdateBrandVoiceResponse(BaseEnvelope):
    data: Optional[dict] = None


# User - me
class CurrentUserData(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class CurrentUserInfoResponse(BaseEnvelope):
    data: Optional[CurrentUserData] = None


# Webhooks - endpoints and events
class WebhookEndpointsListResponse(BaseEnvelope):
    data: Optional[dict] = None


class WebhookEndpointAddResponse(BaseEnvelope):
    data: Optional[dict] = None


class WebhookEndpointUpdateResponse(BaseEnvelope):
    data: Optional[dict] = None


class WebhookEndpointDeleteResponse(BaseEnvelope):
    data: Optional[dict] = None


class WebhookEventsListResponse(BaseEnvelope):
    data: Optional[dict] = None


# Folders
class ListFoldersResponse(BaseEnvelope):
    data: Optional[dict] = None


class CreateFolderRequest(BaseModel):
    name: str
    project_type: Optional[str] = None
    parent_id: Optional[str] = None


class CreateFolderResponse(BaseEnvelope):
    data: Optional[dict] = None


class UpdateFolderRequest(BaseModel):
    name: str


class UpdateFolderResponse(BaseEnvelope):
    data: Optional[dict] = None


class FolderActionResponse(BaseEnvelope):
    data: Optional[dict] = None
