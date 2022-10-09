from fastapi import HTTPException
from service._ import create_user
from schema.index import UserCreateInput, StandardOutput

async def create_user(input: UserCreateInput):
    try:
        await create_user(name=input.name)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))