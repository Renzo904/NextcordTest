from bot.utils.postgre.tables import B
from bot.utils.postgre import Database
from nextcord import Member

class Moderation:
    def __init__(self, bot):
        self.db: Database = bot.db

    async def add_ban(self, user: Member):
        """horeagjlrejalgrea"""
        async with self.db.session_maker() as session:
            async with session.begin():
                session.add(B(data=user.name))
                await session.commit()
        return #bans

    