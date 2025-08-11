import os

import discord

from client import GUILD_ID, client, tree

# Each import automatically registers the command
from commands.about import *
from commands.ai import *
from commands.catfact import *
from commands.cowsays import *
from commands.ping import *


@client.event
async def on_ready():
    print(f"Bot logged as {client.user}")

    activity = discord.Activity(type=discord.ActivityType.listening, name="/ping")
    await client.change_presence(status=discord.Status.online, activity=activity)

    print(f"Commands guild registered:")
    for command in tree.get_commands(guild=GUILD_ID):
        print(f"- {command.name}")


@client.event
async def setup_hook():
    # Sync commands on setup
    await tree.sync(guild=GUILD_ID)
    print(f"Commands synced to guild with ID {GUILD_ID.id}")


# Running discord client
token = os.getenv("DISCORD_TOKEN")
if not token:
    raise EnvironmentError("No DISCORD_TOKEN set")

client.run(token)
