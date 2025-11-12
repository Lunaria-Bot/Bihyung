import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

print(f"[INTENTS] members={intents.members}, message_content={intents.message_content}")

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté : {bot.user.name}#{bot.user.discriminator} (ID: {bot.user.id})")

async def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("❌ DISCORD_TOKEN non défini dans les variables d'environnement Railway.")

    async with bot:
        try:
            await bot.load_extension("cogs.welcome")
            print("[COG] cogs.welcome chargé avec succès.")
        except Exception as e:
            print(f"[ERROR] Échec du chargement du cog welcome : {e}")
async with bot:
        try:
            await bot.load_extension("cogs.formules")
            print("[COG] cogs.formules chargé avec succès.")
        except Exception as e:
            print(f"[ERROR] Échec du chargement du cog formules : {e}")
    
        await bot.start(token)

asyncio.run(main())
