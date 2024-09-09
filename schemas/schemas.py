from pydantic import BaseModel


class Model(BaseModel):
    name: str
    age: int
    city: str
    weight: int
    height: int
    chest: int
    img: list