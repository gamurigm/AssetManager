from pydantic import BaseModel

class Book(BaseModel):
    category: str
    title: str
    path: str

class SearchResult(BaseModel):
    file: str
    line: str
    snippet: str
