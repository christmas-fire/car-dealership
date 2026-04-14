from sqlalchemy.orm import Mapped

from .base import Base

class BrandBase(Base):
    __tablename__ = "brands"

    name: Mapped[str]
    country: Mapped[str]
