from typing import Optional

from pydantic import BaseModel


class ItemSet(BaseModel):
    name: str
    description: Optional[str] = None


class Item(ItemSet):
    id: int


class ItemId(BaseModel):
    ok: bool = True
    id: int
