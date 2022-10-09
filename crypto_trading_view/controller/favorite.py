from fastapi import HTTPException
from service._ import add_favorite
from schema.index import UserAddFavoriteInput, StandardOutput


async def add_to(props: UserAddFavoriteInput):
    try:
        await add_favorite(user_id = props.user_id, symbol = props.symbol)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))