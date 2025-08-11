import discord

from client import GUILD_ID, tree


@tree.command(name="ping", description="Responde con un 'pong'.", guild=GUILD_ID)
async def ping_command(interaction: discord.Interaction):
    await interaction.followup.send("Pong!")
