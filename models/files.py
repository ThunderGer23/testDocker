from typing import Optional
from pydantic import BaseModel

class Files(BaseModel):
    id: Optional[str]
    name: str
    data: bytes