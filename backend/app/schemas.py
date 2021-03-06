from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    user_email: str
    user_first: str
    user_last: str
    user_password: str
    user_location: Optional[str]
    user_description: Optional[str]
    user_profile_picture: Optional[bytes]
    user_is_active: bool
    user_is_admin: bool
    user_skill: Optional[str]
    user_is_medical_professional: bool
    user_is_verified: bool
    user_is_volunteer: bool


class User(UserBase):
    user_email: str
    user_first: str
    user_last: str
    user_skill: Optional[str]
    user_description: Optional[str]
    user_profile_picture: Optional[bytes]
    user_location: Optional[str]
    user_is_active: bool
    user_is_medical_professional: bool
    user_is_verified: bool
    user_is_volunteer: bool


class UpdateUser(BaseModel):
    user_first: Optional[str]
    user_last: Optional[str]
    old_password: Optional[str]
    new_password: Optional[str]
    user_email: Optional[str]
    user_skill: Optional[str]
    user_description: Optional[str]
    user_profile_picture: Optional[bytes]
    user_location: Optional[str]
    user_is_medical_professional: Optional[bool]
    user_is_volunteer: Optional[bool]


class PositionBase(BaseModel):
    position_id: int

    class Config:
        orm_mode = True


class PositionCreate(BaseModel):
    position_name: str


class PositionUpdate(BaseModel):
    position_name: str


class Position(PositionBase):
    position_name: str
