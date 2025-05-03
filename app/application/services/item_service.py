from typing import Optional
from app.domain.models.item import Item
from app.domain.ports.item_repository import ItemRepository

class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def get_item(self, item_id: int) -> Optional[Item]:
        return self.repository.get(item_id)

    def update_item(self, item_id: int, item: Item) -> Item:
        return self.repository.update(item_id, item)
