from sqlalchemy import delete
from database.model.index import Favorite
from sqlalchemy.ext.asyncio.session import async_session

async def add_favorite(user_id: int, symbol: str):
    async with async_session() as session:
        session.add(Favorite(user_id=user_id, symbol=symbol))
        await session.commit()

async def remove_favorite(user_id: int, symbol: str):
    async with async_session() as session:
        await session.execute(delete(Favorite).where(Favorite.user_id == user_id, Favorite.symbol == symbol))
        await session.commit()