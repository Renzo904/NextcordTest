import nextcord
from nextcord.ext import commands
from bot.utils.database.moderation import Moderation


class Chat(commands.Cog, name="Chat"):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.db = Moderation(self.bot)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False and self.bot.user.mentioned_in(message) and len(message.content) == len(self.bot.user.mention):
            await message.channel.send(f'Hello! I am the {self.bot.user.mention}!\nMy Prefix is $')

    @commands.command()
    async def ping(self, ctx):
        print(type(self.db))
        await self.db.add_ban(ctx.author)
        await ctx.reply(f'Tomi se la come')
        