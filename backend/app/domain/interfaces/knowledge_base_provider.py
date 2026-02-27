from abc import ABC, abstractmethod
from typing import List
from ..entities.knowledge_base import Book, SearchResult

class IKnowledgeBaseProvider(ABC):
    @abstractmethod
    def list_books(self) -> List[Book]:
        pass

    @abstractmethod
    def search(self, query: str, limit: int = 5) -> List[SearchResult]:
        pass

    @abstractmethod
    def read_book_section(self, file_path: str, start_line: int, end_line: int) -> str:
        pass
