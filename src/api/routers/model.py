from fastapi import APIRouter, status, Depends, HTTPException

from loguru import logger

from src.api.dependencies import get_model_service
from src.schemas.model import ModelSchema, ModelCreateSchema, ModelUpdateSchema, ModelReadSchema
from src.services.model import ModelService
from src.core.exeptions import ModelNotFound

router = APIRouter(prefix="/models")

@router.get("")
def read_models(model_service: ModelService = Depends(get_model_service)) -> list[ModelSchema]:
    return model_service.list_models()


@router.get("/with-brands")
def read_models_with_brands(service: ModelService = Depends(get_model_service)) -> list[ModelReadSchema]:
    return service.list_models_with_brands()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_model(
    payload: ModelCreateSchema,
    model_service: ModelService = Depends(get_model_service)
) -> ModelSchema:
    return model_service.create_model(model=payload)


@router.patch("/{model_id}")
def update_model(
    model_id: str,
    payload: ModelUpdateSchema,
    model_service: ModelService = Depends(get_model_service)
) -> ModelSchema:
    try:
        return model_service.update_model(model_id=model_id, model_update=payload)
    except ModelNotFound as e:
        logger.exception(e.message)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{model_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_model(model_id: str, model_service: ModelService = Depends(get_model_service)) -> None:
    try:
        return model_service.delete_model(model_id=model_id)
    except ModelNotFound as e:
        logger.exception(e.message)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
