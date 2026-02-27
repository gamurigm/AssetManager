from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IPortfolioRepository(ABC):
    @abstractmethod
    def get_portfolio(self) -> List[Dict[str, Any]]:
        pass
        
    @abstractmethod
    def get_transactions(self) -> List[Dict[str, Any]]:
        pass
        
    # We should also add raw SQL fetching ability since the logic needs it
    @abstractmethod
    def _connect(self, read_only: bool = False):
        pass
