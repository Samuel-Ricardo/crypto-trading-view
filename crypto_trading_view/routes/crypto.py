from connections.crypto import day_summary, day_summary_of
from fastapi import APIRouter


crypto_routes = APIRouter(prefix='/crypto')


@crypto_routes.get('/daily_report/{user_id}')
async def daily_report(user_id:int):
    return await day_summary(user_id)