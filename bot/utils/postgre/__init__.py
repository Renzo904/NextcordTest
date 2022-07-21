from sqlalchemy import create_engine, insert, update
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from os import environ
from .tables import Base

class Database:
    connection_url = environ.get("POSTGRESQL_URI")
    engine = create_async_engine(str(connection_url))
    session_maker: sessionmaker = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    async def start(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def get_session(self):
        async with self.db.session_maker() as session:
            async with session.begin():
                return session

    async def update(self, session, table, *args, **kwargs):
        query = (
                update(table).
                where(args[0]).
                values(kwargs)
                )
        await session.execute(query)

    async def select(self, session, table, *args, **kwargs):
        query = (
                update(table).
                where(args[0]).
                values(kwargs)
                )
        await session.execute(query)