from sqlalchemy.ext.asyncio import AsyncSession
from models.users import User
from sqlalchemy.future import select

class UserService:
    @staticmethod
    async def get_all_users(db: AsyncSession):
        result = await db.execute(select(User))
        return result.scalars().all()
