from datetime import date
from os import getenv


DATABASE_URL = getenv('DATABASE_URL')

def MERCADO_BITCOIN_API_URL(symbol: str, date: date) -> str:
    return f'https://www.mercadobitcoin.net/api/{symbol}/day-summary/{date.year}/{date.month}/{date.day}/'
