from pydantic import BaseModel

# DB
class Article(BaseModel):
    id: int
    name: str
    description: str

