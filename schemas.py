from pydantic import BaseModel
from typing import List  # For Python 3.8 compatibility

class StrategyBase(BaseModel):
    strategy_name: str
    strategy_type: str
    slots: int
    capital: int
    universe: int
    start_date: str
    end_date: str
    stop_loss: float
    take_profit: float

class StrategyCreate(StrategyBase):
    pass

class StrategyShow(StrategyBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 fix
