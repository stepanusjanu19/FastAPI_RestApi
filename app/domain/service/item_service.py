from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.item import Item
from schema.item import ItemCreate, ItemUpdate
from uuid import UUID

class ItemService:
    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Item))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(db: AsyncSession, item_id: UUID):
        return await db.get(Item, item_id)

    @staticmethod
    async def create(db: AsyncSession, item: ItemCreate):
        db_item = Item(**item.dict())
        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        return db_item

    @staticmethod
    async def update(db: AsyncSession, item_id: UUID, item: ItemUpdate):
        db_item = await db.get(Item, item_id)
        if db_item:
            for k, v in item.dict().items():
                setattr(db_item, k, v)
            await db.commit()
            await db.refresh(db_item)
        return db_item

    @staticmethod
    async def delete(db: AsyncSession, item_id: UUID):
        db_item = await db.get(Item, item_id)
        if db_item:
            await db.delete(db_item)
            await db.commit()
        return db_item
