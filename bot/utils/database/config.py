from nextcord import Guild
from bot.utils.postgre import Database
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, update
from bot.utils.postgre.tables import Guilds

class Config:
    def __init__(self, bot):
        self.db: Database = bot.db

    async def get_prefix(self, guild: Guild) -> str:
        session: AsyncSession
        async with self.db.session_maker() as session:
            query = (
                select(Guilds).
                filter_by(guild_id=guild.id)
            )
            response = await session.execute(query)
            guild = response.scalars().first()
            if guild:
                return guild.prefix
            else:
                return None

    async def update_prefix(self, guild: Guild, new_prefix: str):
        session: AsyncSession
        async with self.db.session_maker() as session:
            await self.db.update(session, Guilds, Guilds.guild_id==guild.id, prefix=new_prefix)

            # query = (
            #     select(Guilds).
            #     filter_by(guild_id=guild.id)
            #     )
            # response = await session.execute(query)
            # result: Guilds = response.scalars().first()
            # if not result:
            #     with session.begin():
            #         session.add(Guilds(guild_id=guild.id, prefix=new_prefix))
            # else:
            #     result.prefix = new_prefix
            
            await session.commit()
                    
            # print(result)