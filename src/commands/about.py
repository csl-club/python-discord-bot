import discord

from client import GUILD_ID, tree


@tree.command(name="about", description="Information of bot", guild=GUILD_ID)
async def about_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Sobre mí",
        description="¡Soy un bot creado para divertir!",
        color=discord.Color.random(),
    )
    embed.set_image(
        url="https://super.abril.com.br/wp-content/uploads/2020/09/04-09_gato_SITE.jpg"
    )
    embed.set_footer(text="Gracias por invitarme al servidor :D")

    await interaction.response.send_message(embed=embed)

