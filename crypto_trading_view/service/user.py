from database.model.index import User
from sqlalchemy.ext.asyncio.session import async_session

async def create_user(name: str):
    async with async_session() as session:
        session.add(User(name=name))
        await session.commit()