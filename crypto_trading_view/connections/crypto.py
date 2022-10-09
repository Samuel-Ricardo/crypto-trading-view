from asyncio import gather
from datetime import date, timedelta
from aiohttp import ClientSession
from fastapi import HTTPException
from service.user import get_by_id

from config import MERCADO_BITCOIN_API_URL

async def day_summary(symbol: str):
    async with ClientSession() as session:
        yesterday = date.today() - timedelta(days=1)
        response = await session.get(MERCADO_BITCOIN_API_URL(symbol, yesterday))
        data = await response.json()
        return {
            'highest': data['highest'],
            'lowest': data['lowest'],
            'symbol': symbol
        }

async def day_summary_of(symbol: str, date: date):
    async with ClientSession() as session:
        response = await session.get(MERCADO_BITCOIN_API_URL(symbol, date))
        data = await response.json()
        return {
            'highest': data['highest'],
            'lowest': data['lowest'],
            'symbol': symbol
        }

async def daily_reports(user_id):
    try:
        user = await get_by_id(user_id)
        favorite_symbols = [favorite.symbol for favorite in user.favorites]
        tasks = [day_summary(symbol) for symbol in favorite_symbols]
        return await gather(*tasks)
    except Exception as error:
        raise HTTPException(400, detail=str(error))