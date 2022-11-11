from pydantic import BaseModel
from .article import Article
from typing import List


class Warehouse(BaseModel):
    id: Article
    amount: int
    