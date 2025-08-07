import os
import discord
import asyncio
from client import client, tree, GUILD_ID, model, ai_client
from azure.ai.inference.models import SystemMessage, UserMessage


@tree.command(name="ai", description="AI Integrated", guild=GUILD_ID)
async def cowsay_command(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer(ephemeral=True)

    def do_prompt():
        return ai_client.complete(
        messages=[
            SystemMessage("language base: spanish"), # XD
            UserMessage(prompt),
        ],
        temperature=1.0,
        top_p=1.0,
        model=model)
    
    response = await asyncio.to_thread(do_prompt)
    await interaction.followup.send(response.choices[0].message.content)

