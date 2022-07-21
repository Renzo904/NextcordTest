from nextcord.ext import commands
import nextcord, os
from bot.utils.constants import Client
from bot.utils.postgre import Database
from bot.utils.database.config import Config
from pathlib import Path
import logging

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True


async def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or(Client.default_prefix)(bot, message)
    else:
        try:
            prefix = await Config.get_prefix(bot, message.guild)
            if prefix:
                return commands.when_mentioned_or(prefix)(bot, message)
            else:
                return commands.when_mentioned_or(Client.default_prefix)(bot, message)
        except:
            return commands.when_mentioned_or(Client.default_prefix)(bot, message)
    

bot = commands.AutoShardedBot(command_prefix=get_prefix, intents=intents)


cwd = Path(__file__).parents[0]
cwd = str(cwd)
logging.basicConfig(level=logging.ERROR)
    
@bot.event
async def on_command_error(ctx, error):
    errorEmbed = nextcord.Embed(title="❌ ERROR ❌", color=0xFF2222)
    if isinstance(error, commands.errors.CommandNotFound):
        errorEmbed.add_field(
            name="asd",
            value=str(error)
        )

    await ctx.send(embed = errorEmbed, delete_after=7)

@bot.event
async def on_ready():
    bot.db = Database()
    await bot.db.start()
    print(f"Nextcord version:{nextcord.__version__}")
    print("Bot Ready!")


if __name__ == "__main__":
    try:
        for file in os.listdir(cwd + "/bot/cogs"):
            
            if file.endswith(".py") and not file.startswith("__pycache"):
                bot.load_extension(f"bot.cogs")
                print(f"Loaded {file}")
    except Exception as e:
        print(e)
    
    bot.run(Client.token)
