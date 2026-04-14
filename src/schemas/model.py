from enum import Enum

from pydantic import BaseModel, ConfigDict

from .brand import BrandSchema

class ModelSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    brand_id: str
    name: str
    type: str
         

class ModelType(str, Enum):
    SEDAN = "Sedan"
    HATCHBACK = "Hatchback"
    STATION_WAGON = "Station wagon"
    COUPE = "Coupe"
    SUV = "SUV"
    CABRIOLET = "Cabriolet"


class ModelCreateSchema(BaseModel):
    brand_id: str
    name: str
    type: ModelType
    
    
class ModelUpdateSchema(BaseModel):
    brand_id: str | None = None
    name: str | None = None
    type: ModelType | None = None
    
    
class ModelReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    name: str
    type: ModelType
    brand: BrandSchema
    