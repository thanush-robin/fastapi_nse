from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas, database

from typing import List  # Python 3.8 fix

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/strategies", response_model=schemas.StrategyShow, status_code=201)
def create_strategy(strategy: schemas.StrategyCreate, db: Session = Depends(get_db)):
    db_strategy = models.Strategy(**strategy.dict())
    db.add(db_strategy)
    db.commit()
    db.refresh(db_strategy)
    return db_strategy

@app.get("/strategies", response_model=List[schemas.StrategyShow])
def get_all_strategies(db: Session = Depends(get_db)):
    return db.query(models.Strategy).all()

@app.get("/strategies/{strategy_id}", response_model=schemas.StrategyShow)
def get_strategy(strategy_id: int, db: Session = Depends(get_db)):
    strategy = db.query(models.Strategy).filter(models.Strategy.id == strategy_id).first()
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return strategy

@app.put("/strategies/{strategy_id}", response_model=schemas.StrategyShow)
def update_strategy(strategy_id: int, updated: schemas.StrategyCreate, db: Session = Depends(get_db)):
    strategy = db.query(models.Strategy).filter(models.Strategy.id == strategy_id).first()
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    for key, value in updated.dict().items():
        setattr(strategy, key, value)
    
    db.commit()
    db.refresh(strategy)
    return strategy

@app.delete("/strategies/{strategy_id}", status_code=204)
def delete_strategy(strategy_id: int, db: Session = Depends(get_db)):
    strategy = db.query(models.Strategy).filter(models.Strategy.id == strategy_id).first()
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    db.delete(strategy)
    db.commit()
    return None
