from pydantic import BaseModel


class UserCreateInput(BaseModel):
    name: str

class UserDeleteInput(BaseModel):
    id: int