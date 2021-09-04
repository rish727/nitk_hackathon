from sqlalchemy.orm import Session

from src.models import *
from src.schemas import *

def index():
  return {"status": 200}