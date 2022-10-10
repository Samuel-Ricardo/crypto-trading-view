from fastapi import APIRouter, HTTPException
from schema.index import StandardOutput, ErrorOutput, UserAddFavoriteInput
from service.favorite import add_favorite


favorite_routes = APIRouter(prefix='/favorites')

@favorite_routes.post('/add', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def add_favorite(input: UserAddFavoriteInput):
    try:
        await add_favorite(input.user_id, input.symbol)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

