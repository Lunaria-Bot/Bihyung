import discord
from discord.ext import commands
import asyncio

LOG_CHANNEL_ID = 1438221230539804743

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def log_action(self, ctx, action, target, reason=None):
        """Envoie un log dans le salon dédié."""
        log_channel = ctx.guild.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            embed = discord.Embed(
                title="🛡️ Moderation Log",
                color=discord.Color.red()
            )
            embed.add_field(name="Action", value=action, inline=True)
            embed.add_field(name="Target", value=f"{target} ({target.id})", inline=True)
            embed.add_field(name="Moderator", value=f"{ctx.author} ({ctx.author.id})", inline=True)
            if reason:
                embed.add_field(name="Reason", value=reason, inline=False)
            await log_channel.send(embed=embed)

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"✅ {member.mention} a été **kick**.")
        await self.log_action(ctx, "Kick", member, reason)

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"✅ {member.mention} a été **banni**.")
        await self.log_action(ctx, "Ban", member, reason)

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount+1)  # +1 pour inclure la commande
        await ctx.send(f"🧹 {len(deleted)-1} messages supprimés.", delete_after=5)
        await self.log_action(ctx, f"Purge {amount} messages", ctx.channel)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
