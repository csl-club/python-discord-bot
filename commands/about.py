
from client import tree, GUILD_ID
import discord

@tree.command(name="about", description="Information of bot", guild=GUILD_ID)
async def about_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        """
            Me: GoBot
            Author: salva
            Version: who knows
        """
    )