
from pydantic import BaseModel


class Config:
    orm_mode = True

class StandardOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    detail: str