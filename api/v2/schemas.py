from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field


# Avatars
class Avatar(BaseModel):
    avatar_id: str
    avatar_name: Optional[str] = None
    gender: Optional[str] = None
    preview_image_url: Optional[str] = None
    preview_video_url: Optional[str] = None
    premium: Optional[bool] = None


class TalkingPhoto(BaseModel):
    talking_photo_id: str
    talking_photo_name: Optional[str] = None
    preview_image_url: Optional[str] = None


class AvatarsResponse(BaseModel):
    avatars: List[Avatar] = Field(default_factory=list)
    talking_photos: List[TalkingPhoto] = Field(default_factory=list)


# Voices
class Voice(BaseModel):
    voice_id: str
    language: Optional[str] = None
    gender: Optional[str] = None
    name: Optional[str] = None
    preview_audio: Optional[str] = None
    support_pause: Optional[bool] = None
    emotion_support: Optional[bool] = None
    support_locale: Optional[bool] = None


class VoicesResponse(BaseModel):
    voices: List[Voice] = Field(default_factory=list)


# Locales
class LocaleItem(BaseModel):
    value: Optional[str] = None
    label: Optional[str] = None
    language: Optional[str] = None
    tag: Optional[str] = None
    locale: Optional[str] = None
    language_code: Optional[str] = None


class LocalesResponse(BaseModel):
    data: dict = Field(default_factory=dict)

    @property
    def locales(self) -> List[LocaleItem]:
        items = self.data.get("locales") or []
        return [LocaleItem.model_validate(i) for i in items]


# Avatar Groups
class AvatarGroup(BaseModel):
    id: str
    name: Optional[str] = None
    created_at: Optional[float] = None
    num_looks: Optional[int] = None
    preview_image: Optional[str] = None
    group_type: Optional[str] = None
    train_status: Optional[str] = None
    default_voice_id: Optional[str] = None


class AvatarGroupsResponse(BaseModel):
    total_count: Optional[int] = None
    avatar_group_list: List[AvatarGroup] = Field(default_factory=list)


# Avatars in Group
class GroupAvatar(BaseModel):
    id: str
    image_url: Optional[str] = None
    created_at: Optional[float] = None
    name: Optional[str] = None
    status: Optional[str] = None
    group_id: Optional[str] = None
    is_motion: Optional[bool] = None
    motion_preview_url: Optional[Optional[str]] = None
    business_type: Optional[str] = None
    upscaled: Optional[bool] = None
    background_sound_effect: Optional[Optional[str]] = None
    default_voice_id: Optional[str] = None

    class UpscaleAvailability(BaseModel):
        available: Optional[bool] = None
        reason: Optional[str] = None

    upscale_availability: Optional[UpscaleAvailability] = None


class GroupAvatarsResponse(BaseModel):
    avatar_list: List[GroupAvatar] = Field(default_factory=list)


# Avatar Details
class AvatarDetails(BaseModel):
    type: Optional[str] = None
    id: str
    name: Optional[str] = None
    gender: Optional[str] = None
    preview_image_url: Optional[str] = None
    preview_video_url: Optional[str] = None
    premium: Optional[bool] = None
    is_public: Optional[bool] = None
    default_voice_id: Optional[str] = None
    tags: List[str] = Field(default_factory=list)


class AvatarDetailsResponse(BaseModel):
    error: Optional[str] = None
    data: Optional[AvatarDetails] = None


# Video Translate - Supported Languages
class SupportedLanguagesResponse(BaseModel):
    languages: List[str] = Field(default_factory=list)


# Photo Avatar - Generate Photos
class GeneratePhotoAvatarPhotosRequest(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
    gender: Optional[str] = None
    ethnicity: Optional[str] = None
    orientation: Optional[str] = None
    pose: Optional[str] = None
    style: Optional[str] = None
    appearance: Optional[str] = Field(
        default=None,
        description="Description/Prompt of the generated avatar photo, max 1000 chars",
    )
    callback_url: Optional[str] = None
    callback_id: Optional[str] = None


class GeneratePhotoAvatarPhotosResponse(BaseModel):
    # Response may include additional fields; allow them
    model_config = {"extra": "allow"}
    generation_id: Optional[str] = None


class PhotoAvatarGenerationStatusResponse(BaseModel):
    # Status payloads vary; accept any extra fields
    model_config = {"extra": "allow"}


# User - Remaining Quota (v2)
class RemainingQuotaResponse(BaseModel):
    # The API documents `remaining_quota` and a `details` dict; allow extra for forward-compat
    model_config = {"extra": "allow"}
    remaining_quota: Optional[int] = None
