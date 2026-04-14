from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from src.models.model import ModelBase

class ModelRepository():
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_all(self) -> list[ModelBase]:
        return self.db.scalars(select(ModelBase)).all()
    
    def get_by_id(self, model_id: str) -> ModelBase:
        return self.db.get(ModelBase, model_id)
    
    def get_all_with_brands(self) -> list[ModelBase]:
        query = (
            select(ModelBase)
            .options(joinedload(ModelBase.brand))
        )
        return self.db.scalars(query).unique().all()

    def create(self, brand_id: str, model_name: str, model_type: str) -> ModelBase:
        new_model = ModelBase(brand_id=brand_id, name=model_name, type=model_type)
        self.db.add(new_model)
        return new_model
            
    def delete(self, model: ModelBase) -> None:
        self.db.delete(model)
