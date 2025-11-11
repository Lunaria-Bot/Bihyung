import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import aiohttp
import io

WELCOME_CHANNEL_ID = 1437641570357743618
BACKGROUND_IMAGE_URL = "https://i.imgur.com/1X1X1X1.png"  # Remplace par le lien direct de l'image, pas la page imgur

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.send_welcome(member)

    @commands.command(name="simulate_join")
    async def simulate_join(self, ctx):
        await self.send_welcome(ctx.author)

    async def send_welcome(self, member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if not channel:
            return

        welcome_file = await self.create_welcome_image(member)

        embed = discord.Embed(
            title=f"Hey {member.name} ! 👀 Welcome to {member.guild.name} 👩‍🏭",
            description="Please check [the rules](https://discord.com/channels/1437641569187659928/1437642674294489250)",
            color=discord.Color.purple()
        )
        embed.set_image(url="attachment://welcome.png")
        embed.set_thumbnail(url=member.display_avatar.url)

        await channel.send(file=welcome_file, embed=embed)

    async def create_welcome_image(self, member):
        async with aiohttp.ClientSession() as session:
            # Image de fond
            async with session.get(BACKGROUND_IMAGE_URL) as resp:
                bg_bytes = await resp.read()
            # Avatar
            async with session.get(member.display_avatar.url) as resp:
                avatar_bytes = await resp.read()

        background = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
        avatar = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA").resize((128, 128))

        # Cercle pour avatar
        mask = Image.new("L", avatar.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 128, 128), fill=255)
        avatar.putalpha(mask)

        # Placement avatar
        background.paste(avatar, (50, 50), avatar)

        # Texte
        draw = ImageDraw.Draw(background)
        try:
            font = ImageFont.truetype("arial.ttf", 32)
        except:
            font = ImageFont.load_default()
        draw.text((200, 60), f"Welcome {member.name}!", fill="white", font=font)

        # Sauvegarde
        buffer = io.BytesIO()
        background.save(buffer, format="PNG")
        buffer.seek(0)
        return discord.File(fp=buffer, filename="welcome.png")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
