from typing import List
from ...domain.interfaces.knowledge_base_provider import IKnowledgeBaseProvider
from ...domain.entities.knowledge_base import Book, SearchResult


class SearchKnowledgeBaseUseCase:
    def __init__(self, provider: IKnowledgeBaseProvider):
        self._provider = provider

    def execute(self, query: str, limit: int = 5) -> List[SearchResult]:
        return self._provider.search(query, limit)


class ReadBookSectionUseCase:
    def __init__(self, provider: IKnowledgeBaseProvider):
        self._provider = provider

    def execute(self, file_path: str, start_line: int, end_line: int) -> str:
        return self._provider.read_book_section(file_path, start_line, end_line)
