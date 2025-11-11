import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import aiohttp
import io
import os

WELCOME_CHANNEL_ID = 1437641570357743618
BACKGROUND_IMAGE_PATH = "assets/welcome_bg.png.jpg"

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"[JOIN] {member.name} a rejoint le serveur.")
        await self.send_welcome(member)

    @commands.command(name="simulate_join")
    async def simulate_join(self, ctx):
        print(f"[SIMULATION] Simulation de join pour : {ctx.author.name}")
        await self.send_welcome(ctx.author)

    async def send_welcome(self, member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if not channel:
            print("[ERROR] Salon de bienvenue introuvable.")
            return

        try:
            welcome_file = await self.create_welcome_image(member)
        except Exception as e:
            print(f"[ERROR] Échec de la génération d'image : {e}")
            return

        embed = discord.Embed(
            title=f"Hey {member.name} ! 👀 Welcome to {member.guild.name} 👩‍🏭",
            description="Please check [the rules](https://discord.com/channels/1437641569187659928/1437642674294489250)",
            color=discord.Color.purple()
        )
        embed.set_image(url="attachment://welcome.png")
        embed.set_thumbnail(url=member.display_avatar.url)

        await channel.send(file=welcome_file, embed=embed)
        print(f"[SUCCESS] Message de bienvenue envoyé à {member.name}")

    async def create_welcome_image(self, member):
        async with aiohttp.ClientSession() as session:
            async with session.get(member.display_avatar.url) as resp:
                avatar_bytes = await resp.read()

        background = Image.open(BACKGROUND_IMAGE_PATH).convert("RGBA")
        avatar = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA").resize((128, 128))

        # Cercle pour avatar
        mask = Image.new("L", avatar.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 128, 128), fill=255)
        avatar.putalpha(mask)

        # Placement avatar
        avatar_x = (background.width - avatar.width) // 2
        avatar_y = 300
        background.paste(avatar, (avatar_x, avatar_y), avatar)

        # Texte
        draw = ImageDraw.Draw(background)
        try:
            font = ImageFont.truetype("arial.ttf", 48)
        except:
            font = ImageFont.load_default()

        text = f"Welcome {member.name}!"

        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
        except AttributeError:
            text_width, text_height = font.getsize(text)

        text_x = (background.width - text_width) // 2
        text_y = avatar_y + avatar.height + 20

        # Ombre noire
        draw.text((text_x + 2, text_y + 2), text, fill="black", font=font)
        # Texte blanc
        draw.text((text_x, text_y), text, fill="white", font=font)

        buffer = io.BytesIO()
        background.save(buffer, format="PNG")
        buffer.seek(0)
        return discord.File(fp=buffer, filename="welcome.png")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
