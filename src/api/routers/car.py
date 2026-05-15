from fastapi import APIRouter, status, Depends, HTTPException

from loguru import logger

from src.api.dependencies import get_car_service
from src.schemas.car import CarSchema, CarReadSchema, CarCreateSchema, CarUpdateSchema
from src.services.car import CarService
from src.core.exeptions import CarNotFound

router = APIRouter(prefix="/cars", tags=["cars"])

@router.get("")
def read_cars(car_service: CarService = Depends(get_car_service)) -> list[CarSchema]:
    return car_service.list_cars()


@router.get("/with-models")
def read_cars_with_models(car_service: CarService = Depends(get_car_service)) -> list[CarReadSchema]:
    return car_service.list_cars_with_models()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_car(
    payload: CarCreateSchema,
    car_service: CarService = Depends(get_car_service)
) -> CarSchema:
    return car_service.create_car(car=payload)


@router.patch("/{car_id}")
def update_car(
    car_id: str,
    payload: CarUpdateSchema,
    car_service: CarService = Depends(get_car_service)
) -> CarSchema:
    try:
        return car_service.update_car(car_id=car_id, car_update=payload)
    except CarNotFound as e:
        logger.exception(e.message)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{car_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_car(car_id: str, car_service: CarService = Depends(get_car_service)) -> None:
    try:
        return car_service.delete_car(car_id=car_id)
    except CarNotFound as e:
        logger.exception(e.message)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
