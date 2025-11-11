import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True  # Nécessaire pour détecter les nouveaux membres

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

# Chargement des cogs
bot.load_extension("cogs.welcome")

# Lancement du bot
bot.run(os.getenv("DISCORD_TOKEN"))
