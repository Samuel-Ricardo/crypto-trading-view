from fastapi import HTTPException
from schema.index import UserAddFavoriteInput,\
                         StandardOutput

from service._ import add_favorite,\
                      remove_favorite


async def add_to(props: UserAddFavoriteInput):
    try:
        await add_favorite(user_id = props.user_id, symbol = props.symbol)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


async def remove_of(user_id: int, symbol: str):
    try:
        await remove_favorite(user_id, symbol)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))