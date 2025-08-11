import os

import discord
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()  # Load .env

guild_id_str = os.getenv("GUILD_ID")
if not guild_id_str:
    raise EnvironmentError("No GUILD_ID set")

# My own guild (server)
GUILD_ID = discord.Object(id=guild_id_str)

client = discord.Client(intents=discord.Intents.none())
tree = discord.app_commands.CommandTree(client)
