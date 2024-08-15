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

# User routes

@router.get("/tests/", response_model=List[schemas.Test])
def get_available_tests(db: Session = Depends(get_db)):
    return crud.get_available_tests(db)

@router.post("/{id}/results/", response_model=schemas.Result)
def submit_answers(id: int, result: schemas.ResultCreate, db: Session = Depends(get_db),):
    return crud.submit_answers(db=db, result=result, user_id=id)

@router.get("/{id}/results/{result_id}/", response_model=schemas.Result)
def get_test_result(id:int , result_id: int, db: Session = Depends(get_db)):
    result = crud.get_result(db, result_id=result_id)
    if result.user_id != id:
        raise HTTPException(status_code=403, detail="Not authorized to view this result")
    return result
