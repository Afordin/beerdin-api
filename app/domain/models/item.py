from dataclasses import dataclass
from typing import Optional

@dataclass
class Item:
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None
