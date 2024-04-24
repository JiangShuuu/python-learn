from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

async def get_db():
    async_engine = create_async_engine(DATABASE_URL, echo=True)
    async_session = sessionmaker(
        async_engine, expire_on_commit=False, class_=AsyncSession
    )

    async with async_session() as session:
        yield session

async def create_tables():
    async_engine = create_async_engine(DATABASE_URL)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
