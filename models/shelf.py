from pydantic import BaseModel
from typing import Optional

class Shelf(BaseModel):
    row: int
    bay: int
    height: Optional[float]
    width: Optional[float]
    depth: Optional[float]

    