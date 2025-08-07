from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
import discord
import os

# My own guild (server)
GUILD_ID = discord.Object(id=350914455418306561)

load_dotenv() # Load .env

intents = discord.Intents.default()
intents.message_content = True # Don't forget to enable intents in Developer portal!

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

# Azure AI

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = os.environ["GITHUB_TOKEN"]

ai_client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)
