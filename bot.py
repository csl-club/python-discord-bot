
import os
from client import client, tree, GUILD_ID
import discord

# Each import automatically registers the command
import commands.about as about
import commands.ping as ping
import commands.cowsays as cowsays
import commands.ai as ai

@client.event
async def on_ready():
    print(f"Bot logged as {client.user}")

    activity = discord.Activity(type=discord.ActivityType.playing, name="Minecraft"); # yep

    await client.change_presence(status=discord.Status.online, activity=activity);

    """
    for guild in client.guilds:
        print("guild:", guild)
        await tree.sync(guild=discord.Object(id=guild.id))
    """
    
    print("Commands guild registered:")
    for command in tree.get_commands(guild=GUILD_ID):
        print(f"- {command.name}")

@client.event
async def setup_hook():
    # Register commands manually in setup_hook
    await tree.sync(guild=GUILD_ID)  # sync to your guild
    print(f"Commands synced to guild {GUILD_ID.id}")

if __name__ == "__main__":
    # Running discord client
    apiKey = os.getenv("API_KEY")
    if not apiKey:
        raise EnvironmentError("No API_KEY set")

    client.run(apiKey)