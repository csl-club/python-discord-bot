from client import client, tree, GUILD_ID
import discord
import asyncio


@tree.command(name="ping", description="new pong!", guild=GUILD_ID)
async def ping_command(interaction: discord.Interaction):
    # Async and delayed responses example
    await interaction.response.defer(ephemeral=True, thinking=True);
    await asyncio.sleep(0.5) # half-second delay
    await interaction.followup.send("Pong! ")
