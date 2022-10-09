from sqlalchemy import delete
from database.model.index import User
from sqlalchemy.ext.asyncio.session import async_session

async def create_user(name: str):
    async with async_session() as session:
        session.add(User(name=name))
        await session.commit()

async def delete_user(user_id: int):
    async with async_session() as session:
        await session.execute(delete(User).wwhere(User.id == user_id))
        await session.commit()