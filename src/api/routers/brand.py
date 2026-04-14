from fastapi import APIRouter, status, Depends, HTTPException

from loguru import logger

from src.api.dependencies import get_brand_service
from src.schemas.brand import BrandSchema, BrandCreateSchema, BrandUpdateSchema
from src.services.brand import BrandService
from src.core.exeptions import BrandNotFound

router = APIRouter(prefix="/brands")

@router.get("")
def read_brands(brand_service: BrandService = Depends(get_brand_service)) -> list[BrandSchema]:
    return brand_service.list_brands()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_brand(
    payload: BrandCreateSchema,
    brand_service: BrandService = Depends(get_brand_service)
) -> BrandSchema:
    return brand_service.create_brand(brand=payload)


@router.patch("/{brand_id}")
def update_brand(
    brand_id: str,
    payload: BrandUpdateSchema,
    brand_service: BrandService = Depends(get_brand_service)
) -> BrandSchema:
    try:
        return brand_service.update_brand(brand_id=brand_id, brand_update=payload)
    except BrandNotFound as e:
        logger.exception(e.message)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{brand_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_brand(brand_id: str, brand_service: BrandService = Depends(get_brand_service)) -> None:
    try:
        return brand_service.delete_brand(brand_id=brand_id)
    except BrandNotFound as e:
        logger.exception(e.message)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
