import nextcord
from nextcord.ext import commands
from bot.utils.database.config import Config



class Admin(commands.Cog, name="Admin"):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.db = Config(self.bot)

    @commands.command(aliases=["prefix"])
    @commands.guild_only()
    async def change_prefix(self, ctx: commands.Context, new_prefix: str):
        try:
            await self.db.update_prefix(ctx.guild, new_prefix)
        except Exception as e:
            print(e)
            pass