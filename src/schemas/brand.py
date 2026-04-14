from pydantic import BaseModel, ConfigDict

class BrandSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    name: str
    country: str
         
         
class BrandCreateSchema(BaseModel):
    name: str
    country: str
    
    
class BrandUpdateSchema(BaseModel):
    name: str | None = None
    country: str | None = None
    