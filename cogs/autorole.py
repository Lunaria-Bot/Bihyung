import discord
from discord.ext import commands

# ID du rôle à donner automatiquement
AUTO_ROLE_ID = 1437642831404470443

class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        role = member.guild.get_role(AUTO_ROLE_ID)
        if role:
            try:
                await member.add_roles(role, reason="AutoRole: attribution automatique à l'arrivée")
                print(f"[AUTOROLE] {member} a reçu le rôle {role.name}.")
            except Exception as e:
                print(f"[ERROR] Impossible d'ajouter le rôle à {member}: {e}")
        else:
            print(f"[ERROR] Rôle ID {AUTO_ROLE_ID} introuvable dans {member.guild.name}.")

async def setup(bot):
    await bot.add_cog(AutoRole(bot))
