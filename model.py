from pydantic import BaseModel
from typing import Optional

class FilterRequest(BaseModel):
    filter: Optional[str] = None
    order: Optional[str] = 'asc'
