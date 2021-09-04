# from sqlalchemy.orm import Session

# from src.models import *
# from src.schemas import *

# def login(db: Session, login: Login):
#   # return login.email
#   return db.query(User).filter(User.email == login.email and User.hashed_password == login.password).first()