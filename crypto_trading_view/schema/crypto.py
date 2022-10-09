from pydantic import BaseModel
from commons_schema import Config


class Favorite(BaseModel):
    id:int
    symbol: str
    user_id: int
    config: Config


class DaySummaryOutput(BaseModel):
    highest: float
    lowest: float
    symbol: str