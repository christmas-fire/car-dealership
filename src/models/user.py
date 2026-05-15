import enum
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Role(str, enum.Enum):
    SELLER = "seller"
    CUSTOMER = "customer"


class UserBase(Base):
    __tablename__ = "users"

    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]

    role: Mapped[Role] = mapped_column(Enum(Role), default=Role.SELLER)
