import logging
from os import environ
from typing import NamedTuple
from dotenv import load_dotenv


import nextcord

load_dotenv()

__all__ = (
    "Algolia",
    "Client",
    "Colours",
    "Database",
    "Emojis",
    "Colours",
    "Icons",
    "PasteBin",
    "Stats",
    "Spotify",
    "Tokens",
    "RapidApi",
    "RedirectOutput",
    "ERROR_REPLIES",
    "NEGATIVE_REPLIES",
    "POSITIVE_REPLIES",
)

class Client(NamedTuple):
    name = "Nextcord Template Bot"
    default_prefix = "$"
    guild_id = 932264473408966656
    test_guild_id = 866235308416040971
    bot_version = "1.0.0"
    token = environ.get("BOT_TOKEN")
    debug = environ.get("BOT_DEBUG", "true").lower() == "true"
    invite_permissions = nextcord.Permissions(
        view_channel=True,
        send_messages=True,
        send_messages_in_threads=True,
        manage_messages=True,
        manage_threads=True,
        embed_links=True,
        attach_files=True,
        read_message_history=True,
        add_reactions=True,
        use_external_emojis=True,
        # these are enabled for future features, but not currently used
        change_nickname=True,
        create_public_threads=True,
        create_private_threads=True,
        view_audit_log=True,
    )