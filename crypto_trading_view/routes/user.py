from typing import List
from fastapi import APIRouter
from favorite import favorite_routes
from controller.user import create, delete,  list, get
from schema.commons_schema import StandardOutput, ErrorOutput
from schema.user_schema import UserCreateInput, UserDeleteInput, UserListOutput

user_router = APIRouter(prefix='/user')

@user_router.post('/create', description='Create Users', response_model=StandardOutput, responses= {400: {'model': ErrorOutput}})
async def create_user(input: UserCreateInput):
    return await create(input)


@user_router.delete('/{user_id}', response_model=StandardOutput, responses= {400: {'model': ErrorOutput}})
async def user_delete(user_id: int):
    return await delete(UserDeleteInput(user_id))


@user_router.get("/list", response_model=List[UserListOutput], responses= {400: {'model':ErrorOutput}})
async def list_all():
    return await list()


@user_router.get("/{user_id}", response_model=List[UserListOutput], responses= {400: {'model':ErrorOutput}})
async def get_by_id(user_id: int):
    return await get(user_id)


user_router.include_router(favorite_routes)