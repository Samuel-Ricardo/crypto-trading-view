from typing import List
from fastapi import APIRouter
from controller.user import create, delete,  list
from schema.commons_schema import StandardOutput, ErrorOutput
from schema.user_schema import UserCreateInput, UserDeleteInput, UserListOutput

user_router = APIRouter(prefix='/user')

@user_router.post('/create', description='Create Users', response_model=StandardOutput, responses= {400: {'model': ErrorOutput}})
async def create_user(input: UserCreateInput):
    return create(input)


@user_router.delete('/{user_id}', response_model=StandardOutput, responses= {400: {'model': ErrorOutput}})
async def user_delete(user_id: int):
    return delete(UserDeleteInput(user_id))


@user_router.get("/list", response_model=List[UserListOutput], responses= {400: {'model':ErrorOutput}})
async def list_all():
    return list()