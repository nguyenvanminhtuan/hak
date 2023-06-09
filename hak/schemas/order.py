from pydantic import BaseModel


class OrderCreate(BaseModel):
    url: str


class OrderUpdate(BaseModel):
    state: str
