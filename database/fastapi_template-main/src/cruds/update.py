from sqlalchemy.orm import Session
from src.models import *
from src.schemas import *

def update(db: Session, update: Update):
    user = Informations(name=update.name, date=update.date, information=update.information, url=update.url)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "successed"}