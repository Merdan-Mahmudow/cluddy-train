from typing import Optional
from pydantic import BaseModel


class Model(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None
    weight: Optional[int] = None
    height: Optional[int] = None
    chest: Optional[int] = None
    img: Optional[list[str]] = None
    phone: Optional[str] = None
    cloth: Optional[str] = None
    shoes: Optional[int] = None
    hair: Optional[str] = None
    appereance: Optional[str] = None
    day_1_hour: Optional[int] = None
    day_2_hour: Optional[int] = None
    night_1_hour: Optional[int] = None
    night_all: Optional[int] = None
    class Config:
        from_attributes = True