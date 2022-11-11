from typing import Optional, Binary
from pydantic import BaseModel

class Files(BaseModel):
    id: Optional[str]
    name: str
    data: Binary