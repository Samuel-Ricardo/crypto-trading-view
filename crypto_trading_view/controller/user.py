from fastapi import HTTPException
from service._ import create_user, delete_user
from schema.index import UserCreateInput, UserDeleteInput, StandardOutput

async def create(input: UserCreateInput):
    try:
        await create_user(name=input.name)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


async def delete(input: UserDeleteInput):
    try:
        await delete_user()
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))