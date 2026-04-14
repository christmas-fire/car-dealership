from enum import Enum

from pydantic import BaseModel, ConfigDict

from .model import ModelReadSchema

class TransmissionType(str, Enum):
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"
    RTC = "RTC"
    CVT = "CVT"
    
    
class DriveType(str, Enum):
    FWD = "FWD"
    RWD = "RWD"
    FOUR_BY_FOUR = "4WD"
    AWD = "AWD" 
    
    
class EngineType(str, Enum):
    GASOLINE = "Gasoline"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"


class CarSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    model_id: str
    year: int
    generation: int
    color: str
    price: int
    mileage: int
    transmission: TransmissionType
    drive: DriveType
    engine_cap: float
    engine_type: EngineType
    engine_power: int
    description: str | None = None


class CarCreateSchema(BaseModel):
    model_id: str
    year: int
    generation: int
    color: str
    price: int
    mileage: int
    transmission: TransmissionType
    drive: DriveType
    engine_cap: float
    engine_type: EngineType
    engine_power: int
    description: str | None = None
    
    
class CarUpdateSchema(BaseModel):
    model_id: str | None = None
    year: int | None = None
    generation: int | None = None
    color: str | None = None
    price: int | None = None
    mileage: int | None = None
    transmission: TransmissionType | None = None
    drive: DriveType | None = None
    engine_cap: float | None = None
    engine_type: EngineType | None = None
    engine_power: int | None = None
    description: str | None = None
    
    
class CarReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    year: int
    generation: int
    color: str
    mileage: int
    price: int
    transmission: TransmissionType
    drive: str
    engine_cap: float
    engine_type: EngineType
    engine_power: int
    description: str | None = None   
    model: ModelReadSchema
    