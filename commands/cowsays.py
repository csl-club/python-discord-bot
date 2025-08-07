
from client import tree, GUILD_ID
import discord
import cowsay # Cowsay library

@tree.command(name="cowsay", description="Cow can say?", guild=GUILD_ID)
async def cowsay_command(interaction: discord.Interaction, type: str, text: str):
    if type not in cowsay.char_names:
        await interaction.response.send_message(f"{type} is not a cow type! (Available types: {cowsay.char_names})")
        return

    content = cowsay.get_output_string(type, text)
    await interaction.response.send_message(f"```text\n{content}\n```")