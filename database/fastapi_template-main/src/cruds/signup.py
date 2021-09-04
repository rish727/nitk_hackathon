# from sqlalchemy.orm import Session

# from src.models import *
# from src.schemas import *

# def signup(db: Session, signup: Signup):
#   user = User(email=signup.email, hashed_password=signup.password)
#   db.add(user)
#   db.commit()
#   db.refresh(user)
#   return {"message": "successed"}