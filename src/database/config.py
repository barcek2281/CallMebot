from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from src.database.models import Base, User
import os

load_dotenv()

DB_HOST=os.environ.get("DB_HOST")
DB_NAME=os.environ.get("DB_NAME")
DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_PORT=os.environ.get("DB_PORT")
DB_USER=os.environ.get("DB_USER")

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)     

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
        
async def add_user(user_id: int, username: str, fullname: str):
    async with async_session() as session:
        async with session.begin():
            new_user = User(
                user_id=user_id,
                username=username,
                fullname=fullname
            )
            session.add(new_user) 
            await session.commit()