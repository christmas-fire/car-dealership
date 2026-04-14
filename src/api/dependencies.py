from fastapi import Depends
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.services.brand import BrandService
from src.services.model import ModelService
from src.services.car import CarService

def get_brand_service(db: Session = Depends(get_db)):
    """DI BrandService"""
    return BrandService(db)


def get_model_service(db: Session = Depends(get_db)):
    """DI ModelService"""
    return ModelService(db)


def get_car_service(db: Session = Depends(get_db)):
    """DI CarService"""
    return CarService(db)
