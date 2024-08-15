from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.init_db import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Admin routes


@router.post("/tests/", response_model=schemas.Test)
def create_test(test: schemas.TestCreate, db: Session = Depends(get_db)):
    return crud.create_test(db=db, test=test)

@router.put("/tests/{test_id}/", response_model=schemas.Test)
def update_test(test_id: int, test: schemas.TestCreate, db: Session = Depends(get_db)):
    db_test = crud.get_test(db, test_id=test_id)
    if not db_test:
        raise HTTPException(status_code=404, detail="Test not found")
    return crud.update_test(db=db, test_id=test_id, test=test)

@router.delete("/tests/{test_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_test(test_id: int, db: Session = Depends(get_db)):
    db_test = crud.get_test(db, test_id=test_id)
    if not db_test:
        raise HTTPException(status_code=404, detail="Test not found")
    crud.delete_test(db=db, test_id=test_id)
    return None

@router.get("/results/", response_model=List[schemas.Result])
def get_all_results(db: Session = Depends(get_db)):
    return crud.get_all_results(db)
