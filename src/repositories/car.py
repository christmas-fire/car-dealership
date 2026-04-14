from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from src.models.car import CarBase
from src.models.model import ModelBase

class CarRepository():
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_all(self) -> list[CarBase]:
        return self.db.scalars(select(CarBase)).all()
    
    def get_by_id(self, car_id: str) -> CarBase:
        return self.db.get(CarBase, car_id)
    
    def get_all_with_models(self) -> list[CarBase]:
        query = (
            select(CarBase)
            .options(joinedload(CarBase.model))
        )
        return self.db.scalars(query).unique().all()

    def create(
        self,
        model_id: str,
        year: int,
        generation: int,
        color: str,
        price: int,
        mileage: int,
        transmission: str,
        drive: str,
        engine_cap: float,
        engine_type: str,
        engine_power: int,
        description: str | None = None,
    ) -> ModelBase:
        new_car = CarBase(
            model_id=model_id,
            year=year,
            generation=generation,
            color=color,
            price=price,
            mileage=mileage,
            transmission=transmission,
            drive=drive,
            engine_cap=engine_cap,
            engine_type=engine_type,
            engine_power=engine_power,
            description=description
        )
        self.db.add(new_car)
        return new_car
            
    def delete(self, car: CarBase) -> None:
        self.db.delete(car)
