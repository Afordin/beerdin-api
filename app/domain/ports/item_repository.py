from abc import ABC, abstractmethod
from typing import Optional
from app.domain.models.item import Item

class ItemRepository(ABC):

    @abstractmethod
    def get(self, item_id: int) -> Optional[Item]:
        pass

    @abstractmethod
    def update(self, item_id: int, item: Item) -> Item:
        pass
