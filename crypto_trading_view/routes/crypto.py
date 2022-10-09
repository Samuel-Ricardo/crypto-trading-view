from typing import List
from connections.crypto import daily_reports, reports_in_interval
from schema.index import DaySummaryOutput, ErrorOutput
from fastapi import APIRouter


crypto_routes = APIRouter(prefix='/crypto')


@crypto_routes.get('/daily_report/{user_id}', response_model = List[DaySummaryOutput], responses={400: {'model': ErrorOutput}})
async def daily_report(user_id:int):
    return await daily_reports(user_id)


@crypto_routes.get('/daily_report/{user_id}/interval/{interval}', response_model = List[DaySummaryOutput], responses={400: {'model': ErrorOutput}})
async def reports(user_id:int, interval:int):
    return await reports_in_interval(user_id, interval)