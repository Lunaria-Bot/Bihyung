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

# Commande admin pour recharger un cog à chaud
@bot.command(name="reload")
@commands.has_permissions(administrator=True)
async def reload(ctx, extension: str):
    try:
        await bot.unload_extension(f"cogs.{extension}")
        await bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"🔄 Cog **{extension}** rechargé avec succès.")
        print(f"[RELOAD] Cog {extension} rechargé.")
    except Exception as e:
        await ctx.send(f"❌ Impossible de recharger {extension} : {e}")
        print(f"[ERROR] Reload {extension} : {e}")

async def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("❌ DISCORD_TOKEN non défini dans les variables d'environnement Railway.")

    async with bot:
        # Charger automatiquement tous les cogs du dossier "cogs"
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                cog_name = f"cogs.{filename[:-3]}"
                try:
                    await bot.load_extension(cog_name)
                    print(f"[COG] {cog_name} chargé avec succès.")
                except Exception as e:
                    print(f"[ERROR] Échec du chargement du cog {cog_name} : {e}")

        await bot.start(token)

asyncio.run(main())
