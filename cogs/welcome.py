import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import aiohttp
import io

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 1437641570357743618
        channel = member.guild.get_channel(channel_id)
        if not channel:
            return

        # Création de l'image de bienvenue
        welcome_image = await self.create_welcome_image(member)

        # Message d'accueil
        embed = discord.Embed(
            title=f"Hey {member.name} ! 👀 Welcome to {member.guild.name} 👩‍🏭",
            description="Please check [the rules](https://discord.com/channels/1437641569187659928/1437642674294489250)",
            color=discord.Color.purple()
        )
        embed.set_image(url="attachment://welcome.png")
        embed.set_thumbnail(url=member.display_avatar.url)

        await channel.send(file=welcome_image, embed=embed)

    async def create_welcome_image(self, member):
        base_url = "https://imgur.com/a/CZW6Zvc"  # Remplace par ton image de fond
        async with aiohttp.ClientSession() as session:
            async with session.get(base_url) as resp:
                background_bytes = await resp.read()
            async with session.get(member.display_avatar.url) as resp:
                avatar_bytes = await resp.read()

        background = Image.open(io.BytesIO(background_bytes)).convert("RGBA")
        avatar = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA").resize((128, 128))

        # Cercle pour l'avatar
        mask = Image.new("L", avatar.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 128, 128), fill=255)
        avatar.putalpha(mask)

        # Placement
        background.paste(avatar, (50, 50), avatar)

        # Texte
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("arial.ttf", 32)
        draw.text((200, 60), f"Welcome {member.name}!", fill="white", font=font)

        # Sauvegarde
        buffer = io.BytesIO()
        background.save(buffer, format="PNG")
        buffer.seek(0)
        return discord.File(fp=buffer, filename="welcome.png")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
