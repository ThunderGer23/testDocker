from typing import Optional
from pydantic import BaseModel

# The User class is a subclass of BaseModel, and it has four attributes: id, name, email, and password
class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str