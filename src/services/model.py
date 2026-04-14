from sqlalchemy.orm import Session

from src.repositories.model import ModelRepository
from src.schemas.model import ModelSchema, ModelCreateSchema, ModelUpdateSchema, ModelReadSchema
from src.core.exeptions import ModelNotFound

class ModelService():
    def __init__(self, db: Session) -> None:
        self.db = db
        self.model_repository = ModelRepository(db)
        
    def list_models(self) -> list[ModelSchema]:
        models_orm = self.model_repository.get_all()
        return [ModelSchema.model_validate(model) for model in models_orm]
    
    def list_models_with_brands(self) -> list[ModelReadSchema]:
        models_orm = self.model_repository.get_all_with_brands()
        return [ModelReadSchema.model_validate(model) for model in models_orm]
    
    def create_model(self, model: ModelCreateSchema) -> ModelSchema:
        model_orm = self.model_repository.create(
            brand_id=model.brand_id,
            model_name=model.name,
            model_type=model.type
        )
        self.db.commit()
        return ModelSchema.model_validate(model_orm)
 
    def update_model(self, model_id: str, model_update: ModelUpdateSchema) -> ModelSchema:
        model_to_update = self.model_repository.get_by_id(model_id=model_id)
        if not model_to_update:
            raise ModelNotFound(f"Model with id={model_id} not found")
        
        if model_update.brand_id is not None:
            model_to_update.brand_id = model_update.brand_id
        if model_update.name is not None:
            model_to_update.name = model_update.name
        if model_update.type is not None:
            model_to_update.type = model_update.type
    
        self.db.commit()
        return ModelSchema.model_validate(model_to_update)
    
    def delete_model(self, model_id: str) -> None:
        model_for_delete = self.model_repository.get_by_id(model_id=model_id)
        if not model_for_delete:
            raise ModelNotFound(f"Model with id={model_id} not found")
        
        self.model_repository.delete(model_for_delete)
        self.db.commit()
        