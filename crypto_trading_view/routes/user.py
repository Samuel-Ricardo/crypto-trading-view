from fastapi import APIRouter
from controller.user import create, delete,  list
from schema.commons_schema import StandardOutput, ErrorOutput
from schema.user_schema import UserCreateInput, UserDeleteInput, UserListOutput

user_router = APIRouter(prefix='/user')

@user_router.post('/create', description='My description', response_model=StandardOutput, responses= {400: {'model': ErrorOutput}})
async def create_user(input: UserCreateInput):
    return create(input)

async def user_delete(user_id: int):
    delete(UserDeleteInput(user_id))