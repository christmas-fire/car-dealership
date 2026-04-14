from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .model import ModelBase

class CarBase(Base):
    __tablename__ = "cars"

    model_id: Mapped[str] = mapped_column(
        ForeignKey("models.id", ondelete="CASCADE")
    )
    year: Mapped[int]
    generation: Mapped[int]
    color: Mapped[str]
    price: Mapped[int]
    mileage: Mapped[int]
    transmission: Mapped[str]
    drive: Mapped[str]
    engine_cap: Mapped[float]
    engine_type: Mapped[str]
    engine_power: Mapped[int]
    description: Mapped[str | None] = mapped_column(nullable=True, default=None)
    
    model: Mapped["ModelBase"] = relationship("ModelBase")
    