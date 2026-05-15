from enum import Enum

from pydantic import BaseModel, EmailStr, ConfigDict

class Role(str, Enum):
    SELLER = "seller"
    CUSTOMER = "customer"


class UserSchema(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str


class UserUpdateSchema(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    role: str | None = None
