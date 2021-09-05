from typing import List, Optional

from pydantic import BaseModel

"""
class AddInfo(BaseModel):
    name : str
    date : int
    information : str
    url : str
"""

class Update(BaseModel):
    name: str
    date: int
    information: str
    url: str
    
class Output(BaseModel):
    name: str
    date: int
    information: str
    url: str
    
    

