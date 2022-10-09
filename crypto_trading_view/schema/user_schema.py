from typing import List
from pydantic import BaseModel

import symbol


class UserCreateInput(BaseModel):
    name: str

class UserDeleteInput(BaseModel):
    id: int

class UserAddFavoriteInput(BaseModel):
    user_id: int
    symbol: str

class UserListOutput(BaseModel):
    id:int
    name:str
    favoites: List[Favorite]

    class config:
        orm_mode = True