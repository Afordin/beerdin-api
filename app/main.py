from typing import Union
from typing import List
from fastapi import FastAPI


from app.domain.models.item import Item
from app.infrastructure.persistence.local_item_repository import LocalItemRepository

app = FastAPI()
repository = LocalItemRepository()


@app.get("/", response_model=List[Item])
def get_all_items():
    return list(repository.items.values())

