import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")

async def main():
    async with bot:
        await bot.load_extension("cogs.welcome")
        await bot.start(os.getenv("DISCORD_TOKEN"))

asyncio.run(main())
