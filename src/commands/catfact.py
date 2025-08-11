import discord
import requests

from client import GUILD_ID, tree


@tree.command(
    name="catfact", description="Muestra un dato random sobre gatos", guild=GUILD_ID
)
async def catfact_command(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    await interaction.followup.send(data["fact"])
