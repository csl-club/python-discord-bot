import asyncio
import os

import discord
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

from client import GUILD_ID, tree

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = os.environ["GITHUB_TOKEN"]

ai_client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


@tree.command(
    name="ai", description="Responde a tu mensaje con ✨ IA ✨", guild=GUILD_ID
)
async def cowsay_command(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer(ephemeral=True)

    def complete_prompt():
        return ai_client.complete(
            messages=[
                SystemMessage("language base: spanish"),  # XD
                UserMessage(prompt),
            ],
            temperature=1.0,
            top_p=1.0,
            model=model,
        )

    response = await asyncio.to_thread(complete_prompt)
    await interaction.followup.send(response.choices[0].message.content)
