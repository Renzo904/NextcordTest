from bot.cogs import Chat, Admin
def unload(bot) -> None:
    """
    Reinstates the original help command.
    This is run if the cog raises an exception on load, or if the extension is unloaded.
    """
    bot._old_help = bot.get_command("help")
    bot.remove_command("help")
    bot.add_command(bot._old_help)

def teardown(bot) -> None:
    """
    The teardown for the help extension.
    This is called automatically on `bot.unload_extension` being run.
    Calls `unload` in order to reinstate the original help command.
    """
    unload(bot)

def setup(bot):
    bot.add_cog(Chat.Chat(bot))
    bot.add_cog(Admin.Admin(bot))