from typing import Annotated
from repository import ItemRepository
from fastapi import Depends, APIRouter
from schemas import ItemSet, Item, ItemId


router = APIRouter(
    prefix="/items",
)


@router.get("")
async def get_items() -> list[Item]:
    items = await ItemRepository.get_all()
    return items


@router.post("")
async def create_item(
        item: Annotated[ItemSet, Depends()]
) -> ItemId:
    item_id = await ItemRepository.create(item)
    return {"ok": True, "id": item_id}
