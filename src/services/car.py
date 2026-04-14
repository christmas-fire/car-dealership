from sqlalchemy.orm import Session

from src.repositories.car import CarRepository
from src.schemas.car import CarSchema, CarReadSchema, CarCreateSchema, CarUpdateSchema
from src.core.exeptions import CarNotFound

class CarService():
    def __init__(self, db: Session) -> None:
        self.db = db
        self.car_repository = CarRepository(db)
        
    def list_cars(self) -> list[CarSchema]:
        cars_orm = self.car_repository.get_all()
        return [CarSchema.model_validate(car) for car in cars_orm]
    
    def list_cars_with_models(self) -> list[CarReadSchema]:
        cars_orm = self.car_repository.get_all_with_models()
        return [CarReadSchema.model_validate(car) for car in cars_orm]
    
    def create_car(self, car: CarCreateSchema) -> CarSchema:
        car_orm = self.car_repository.create(
            model_id=car.model_id,
            year=car.year,
            generation=car.generation,
            color=car.color,
            price=car.price,
            mileage=car.mileage,
            transmission=car.transmission,
            drive=car.drive,
            engine_cap=car.engine_cap,
            engine_type=car.engine_type,
            engine_power=car.engine_power,
            description=car.description
        )
        self.db.commit()
        return CarSchema.model_validate(car_orm)
 
    def update_car(self, car_id: str, car_update: CarUpdateSchema) -> CarSchema:
        car_to_update = self.car_repository.get_by_id(car_id=car_id)
        if not car_to_update:
            raise CarNotFound(f"Car with id={car_id} not found")
        
        update_data = car_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(car_to_update, field, value)
    
        self.db.commit()
        return CarSchema.model_validate(car_to_update)
    
    def delete_car(self, car_id: str) -> None:
        car_for_delete = self.car_repository.get_by_id(car_id=car_id)
        if not car_for_delete:
            raise CarNotFound(f"Car with id={car_id} not found")
        
        self.car_repository.delete(car_for_delete)
        self.db.commit()
        