from pydantic import BaseModel
from typing import List, Optional
import enum

class UserRole(str, enum.Enum):
    admin = "admin"
    user = "user"

class UserCreate(BaseModel):
    username: str
    password: str
    role: UserRole

class User(BaseModel):
    id: int
    username: str
    role: UserRole

    class Config:
        orm_mode = True

class TestCreate(BaseModel):
    title: str
    description: Optional[str] = None

class Test(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    text: str
    test_id: int

class Question(BaseModel):
    id: int
    text: str
    test_id: int

    class Config:
        orm_mode = True

class AnswerCreate(BaseModel):
    text: str
    is_correct: bool
    question_id: int

class Answer(BaseModel):
    id: int
    text: str
    is_correct: bool
    question_id: int

    class Config:
        orm_mode = True

class ResultCreate(BaseModel):
    test_id: int
    score: int

class Result(BaseModel):
    id: int
    user_id: int
    test_id: int
    score: int

    class Config:
        orm_mode = True
