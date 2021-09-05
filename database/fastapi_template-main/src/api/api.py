import json
from typing import List, Optional
from src import cruds

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from src import cruds
from src.database import get_db
from src.schemas.schemas import *


router = APIRouter()

@router.get('/bootup')
def index():
    json_data = cruds.bootup.index()
    if not json_data:
        raise HTTPException(status_code=405, detail='not found')
    return json_data

@router.post('/update')
def update(update: Update, db: Session=Depends(get_db)):
    json_data = cruds.update.update(db, update=update)
    if not json_data:
        raise HTTPException(status_code=404, detail='Account not found')
    return json_data

@router.post('/output')
def output(db: Session = Depends(get_db)):
    json_data = cruds.output.output(db)
    if not json_data:
        raise HTTPException(status_code=404, detail='Account not found')
    return json_data  #{"message": "successed"}

# @router.post('/signup')
# def signup(signup: Signup, db: Session = Depends(get_db)):
#     json_data = cruds.signup.signup(db, signup=signup)
#     if not json_data:
#         raise HTTPException(status_code=404, detail='Todo not found')
#     return json_data

# @router.get('/todo', response_model=List[TodoModel])
# def index(limit: Optional[int] = 100, db: Session = Depends(get_db)):
#     json_data = cruds.todo.index(db, limit=limit)
#     if not json_data:
#         raise HTTPException(status_code=404, detail='Todo not found')
#     return json_data

# @router.post('/todo')
# def create(todo: TodoCreate, db: Session = Depends(get_db)):
#     json_data = cruds.todo.create(db, todo=todo)
#     if not json_data:
#         raise HTTPException(status_code=404, detail='Todo not found')
#     return {"message": "successed"}

# @router.get('/user/{email}', response_model=UserModel)
# def show(email: str, db: Session = Depends(get_db)):
#     json_data = cruds.user.show(db, email=email)
#     if not json_data:
#         raise HTTPException(status_code=404, detail='Todo not found')
#     return {"email":email, "todos": json_data}

# @router.post('/ml', response_model=MlResponse)
# def ml(data: MlData):
#     json_data = cruds.ml.ml(data=data)
#     if not json_data:
#         raise HTTPException(status_code=405, detail='Todo not found')
#     print(json_data)
#     return json_data
