"""
Category Service with Sqlalchemy ORM
"""
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from model.category import Category


class CategoryService:
    """
    Class Category Service
    with Sqlalchemy ORM
    """
    async def get_all(self, async_session: async_sessionmaker[AsyncSession]):
        """
        Get all category objects from db
        """
        async with async_session() as session:
            statement = select(Category).order_by(Category.id)

            result = await session.execute(statement)

            return result.scalars()

    async def create(self, async_session: async_sessionmaker[AsyncSession], category: Category):
        """
        Create category object
        """
        async with async_session() as session:
            session.add(category)
            await session.commit()

        return category

    async def get_by_id(
        self, async_session: async_sessionmaker[AsyncSession], category_id: str
    ):
        """
        Get category by id
        """
        async with async_session() as session:
            statement = select(Category).filter(Category.id == category_id)

            result = await session.execute(statement)

            category = result.scalars().one()

            return category.to_dict()

    async def update(
        self, async_session: async_sessionmaker[AsyncSession], category_id, data
    ):
        """
        Update category by id
        """
        print("update")
        async with async_session() as session:
            statement = select(Category).filter(Category.id == category_id)

            result = await session.execute(statement)

            category = result.scalars().one()

            category.name = data["name"]
            category.description = data["description"]

            await session.commit()

            return category

    async def delete(self, async_session: async_sessionmaker[AsyncSession], category_id: str):
        """delete category by id
        """
        print("delete")
        async with async_session() as session:
            statement = select(Category).filter(Category.id == category_id)
            result_category = await session.execute(statement)
            category = result_category.scalars().one()
            await session.delete(category)
            await session.commit()
