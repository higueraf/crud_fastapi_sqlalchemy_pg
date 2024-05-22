"""
Create Table Category with sqlalchemy
"""
import asyncio

from db import Base, engine


async def create_db():
    """
    Create Table in Database
    """
    async with engine.begin() as conn_alchemy:
        from model.category import Category
        await conn_alchemy.run_sync(Base.metadata.drop_all)
        await conn_alchemy.run_sync(Base.metadata.create_all)

    await engine.dispose()

asyncio.run(create_db())