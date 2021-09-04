# from sqlalchemy.orm import Session

# from src.models import *
# from src.schemas import *

# def index(db: Session, limit):
#   return db.query(Todo).limit(limit).all()

# def create(db: Session, todo: TodoCreate):
#   new_todo = Todo(title=todo.title, text=todo.text, owner_id=todo.owner_id)
#   db.add(new_todo)
#   db.commit()
#   db.refresh(new_todo)
#   return new_todo