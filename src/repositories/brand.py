from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.brand import BrandBase

class BrandRepository():
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_all(self) -> list[BrandBase]:
        return self.db.scalars(select(BrandBase)).all()
    
    def get_by_id(self, brand_id: str) -> BrandBase:
        return self.db.get(BrandBase, brand_id)

    def create(self, brand_name: str, brand_country: str) -> BrandBase:
        new_brand = BrandBase(name=brand_name, country=brand_country)
        self.db.add(new_brand)
        return new_brand
            
    def delete(self, brand: BrandBase) -> None:
        self.db.delete(brand)
