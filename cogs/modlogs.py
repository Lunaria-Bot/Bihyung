import discord
from discord.ext import commands

LOG_CHANNEL_ID = 1438221230539804743  # Salon des logs

class ModLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_log_channel(self, guild):
        return guild.get_channel(LOG_CHANNEL_ID)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        log_channel = self.get_log_channel(message.guild)
        if log_channel:
            embed = discord.Embed(
                title="🗑️ Message Deleted",
                color=discord.Color.red()
            )
            embed.add_field(name="Author", value=f"{message.author} ({message.author.id})", inline=True)
            embed.add_field(name="Channel", value=message.channel.mention, inline=True)
            embed.add_field(name="Content", value=message.content or "*No content*", inline=False)
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            return
        if before.content == after.content:
            return
        log_channel = self.get_log_channel(before.guild)
        if log_channel:
            embed = discord.Embed(
                title="✏️ Message Edited",
                color=discord.Color.orange()
            )
            embed.add_field(name="Author", value=f"{before.author} ({before.author.id})", inline=True)
            embed.add_field(name="Channel", value=before.channel.mention, inline=True)
            embed.add_field(name="Before", value=before.content or "*No content*", inline=False)
            embed.add_field(name="After", value=after.content or "*No content*", inline=False)
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        log_channel = self.get_log_channel(invite.guild)
        if log_channel:
            embed = discord.Embed(
                title="🎟️ Invite Created",
                color=discord.Color.green()
            )
            embed.add_field(name="Code", value=invite.code, inline=True)
            embed.add_field(name="Channel", value=invite.channel.mention, inline=True)
            embed.add_field(name="Inviter", value=f"{invite.inviter} ({invite.inviter.id})", inline=True)
            embed.add_field(name="Max Uses", value=str(invite.max_uses) if invite.max_uses else "Unlimited", inline=True)
            embed.add_field(name="Expires At", value=str(invite.expires_at) if invite.expires_at else "Never", inline=True)
            await log_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ModLogs(bot))
