from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from app.application.services.item_service import ItemService
from app.infrastructure.persistence.local_item_repository import LocalItemRepository


router = APIRouter()
service = ItemService(LocalItemRepository())

class ItemRequest(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@router.get("/items/{item_id}")
def get_item(item_id: int):
    item = service.get_item(item_id)
    if item is None:
        return {"error": "Item no encontrado"}
    return item.__dict__

@router.put("/items/{item_id}")
def update_item(item_id: int, request: ItemRequest):
    item = service.update_item(item_id, request.model_dump() | {"id": item_id})
    return item.__dict__
