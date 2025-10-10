from typing import Optional
from pydantic import BaseModel

class Register(BaseModel):
    name: str
    email: str
    password: str
    gender: Optional[str] = None
