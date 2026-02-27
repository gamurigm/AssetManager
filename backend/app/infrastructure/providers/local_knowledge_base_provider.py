import os
import subprocess
from typing import List
from pathlib import Path
from ...domain.interfaces.knowledge_base_provider import IKnowledgeBaseProvider
from ...domain.entities.knowledge_base import Book, SearchResult

KB_ROOT = Path("C:/AssetManager/data/quant_kb")

class LocalKnowledgeBaseProvider(IKnowledgeBaseProvider):
    def __init__(self, root_path: Path = KB_ROOT):
        self.root_path = root_path

    def list_books(self) -> List[Book]:
        books = []
        if not self.root_path.exists():
            return []
            
        for category_dir in self.root_path.iterdir():
            if category_dir.is_dir():
                category = category_dir.name
                for file in category_dir.glob("*.md"):
                    books.append(Book(
                        category=category,
                        title=file.stem,
                        path=str(file)
                    ))
        return books

    def search(self, query: str, limit: int = 5) -> List[SearchResult]:
        results = []
        if not self.root_path.exists():
            return []

        try:
            cmd = ["powershell", "-Command", f"Select-String -Path '{self.root_path}\\**\\*.md' -Pattern '{query}' | Select-Object -First {limit}"]
            process = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
            
            if process.stdout:
                for line in process.stdout.strip().split('\n'):
                    parts = line.split(':', 2)
                    if len(parts) >= 3:
                        path_str = parts[0].strip()
                        line_num = parts[1].strip()
                        content = parts[2].strip()
                        results.append(SearchResult(
                            file=os.path.basename(path_str),
                            line=line_num,
                            snippet=content
                        ))
        except Exception:
            for book in self.list_books():
                with open(book.path, "r", encoding="utf-8") as f:
                    for i, line in enumerate(f, 1):
                        if query.lower() in line.lower():
                            results.append(SearchResult(
                                file=book.title,
                                line=str(i),
                                snippet=line.strip()
                            ))
                            if len(results) >= limit:
                                return results
        return results

    def read_book_section(self, file_path: str, start_line: int, end_line: int) -> str:
        if not os.path.exists(file_path):
            return "File not found."
            
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                total = len(lines)
                start = max(0, start_line - 1)
                end = min(total, end_line)
                return "".join(lines[start:end])
        except Exception as e:
            return f"Error reading file: {str(e)}"
