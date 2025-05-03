from app.domain.models.item import Item
from app.domain.ports.item_repository import ItemRepository

class LocalItemRepository(ItemRepository):
    def __init__(self):
        self.items = {
            1: Item(id=1, name="Cerveza Afor", price=5.5),
            2: Item(id=2, name="Cerveza Capibara", price=4.5),
        }

    def get(self, item_id: int):
        return self.items.get(item_id)

    def update(self, item_id: int, item: Item):
        self.items[item_id] = item
        return item
