from sqlalchemy import select

from db import new_session, ItemOrm
from schemas import Item, ItemSet


class ItemRepository:
    @classmethod
    async def get(cls, item_id):
        pass

    @classmethod
    async def get_all(cls) -> list[Item]:
        async with new_session() as session:
            query = select(ItemOrm)
            result = await session.execute(query)

            item_models = result.scalars().all()
            return item_models

    @classmethod
    async def create(cls, item: ItemSet) -> int:
        async with new_session() as session:
            item_dict = item.model_dump()
            new_item = ItemOrm(**item_dict)

            session.add(new_item)
            await session.flush()
            await session.commit()
            return new_item.id

    @classmethod
    async def delete(cls, item_id):
        pass

    @classmethod
    async def update(cls, item_id, item):
        pass
