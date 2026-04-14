from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .brand import BrandBase

class ModelBase(Base):
    __tablename__ = "models"

    brand_id: Mapped[str] = mapped_column(
        ForeignKey("brands.id", ondelete="CASCADE")
    )
    name: Mapped[str]
    type: Mapped[str]
    
    brand: Mapped["BrandBase"] = relationship("BrandBase")
    