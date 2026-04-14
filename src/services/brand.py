from sqlalchemy.orm import Session

from src.repositories.brand import BrandRepository
from src.schemas.brand import BrandSchema, BrandCreateSchema, BrandUpdateSchema
from src.core.exeptions import BrandNotFound

class BrandService():
    def __init__(self, db: Session) -> None:
        self.db = db
        self.brand_repository = BrandRepository(db)
        
    def list_brands(self) -> list[BrandSchema]:
        brands_orm = self.brand_repository.get_all()
        return [BrandSchema.model_validate(brand) for brand in brands_orm]
    
    def create_brand(self, brand: BrandCreateSchema) -> BrandSchema:
        brand_orm = self.brand_repository.create(
            brand_name=brand.name,
            brand_country=brand.country
        )
        self.db.commit()
        return BrandSchema.model_validate(brand_orm)
 
    def update_brand(self, brand_id: str, brand_update: BrandUpdateSchema) -> BrandSchema:
        brand_to_update = self.brand_repository.get_by_id(brand_id=brand_id)
        if not brand_to_update:
            raise BrandNotFound(f"Brand with id={brand_id} not found")
        
        if brand_update.name is not None:
            brand_to_update.name = brand_update.name
        if brand_update.country is not None:
            brand_to_update.country = brand_update.country
    
        self.db.commit()
        return BrandSchema.model_validate(brand_to_update)
    
    def delete_brand(self, brand_id: str) -> None:
        brand_for_delete = self.brand_repository.get_by_id(brand_id=brand_id)
        if not brand_for_delete:
            raise BrandNotFound(f"Brand with id={brand_id} not found")
        
        self.brand_repository.delete(brand_for_delete)
        self.db.commit()
        