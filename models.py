from sqlalchemy import Column, Integer, String, Float
from database import Base

class Strategy(Base):
    __tablename__ = "strategies"

    id = Column(Integer, primary_key=True, index=True)
    strategy_name = Column(String)
    strategy_type = Column(String)
    slots = Column(Integer)
    capital = Column(Integer)
    universe = Column(Integer)
    start_date = Column(String)
    end_date = Column(String)
    stop_loss = Column(Float)
    take_profit = Column(Float)
