import discord
from discord.ext import commands

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rules")
    async def show_rules(self, ctx):
        embed = discord.Embed(
            title="📜 Server Rules",
            color=discord.Color.dark_red()
        )

        embed.add_field(
            name="🚫 Content Restrictions",
            value=(
                "• No obscene or explicit content\n"
                "• No NSFW content\n"
                "• No sensitive topics (race, religion, politics)"
            ),
            inline=False
        )

        embed.add_field(
            name="🤝 Respect & Behavior",
            value=(
                "• Treat everyone with respect\n"
                "• No harassment, bullying, or hate speech\n"
                "• Avoid drama or arguments — take it to DMs"
            ),
            inline=False
        )

        embed.add_field(
            name="📌 Channel Usage",
            value=(
                "• Use appropriate channels for each topic\n"
                "• Speak English so everyone can understand"
            ),
            inline=False
        )

        embed.add_field(
            name="📢 Advertising",
            value=(
                "• No advertising without explicit permission\n"
                "• This includes unsolicited DMs"
            ),
            inline=False
        )

        embed.add_field(
            name="📎 Community Guidelines",
            value="[Follow Discord's Community Guidelines](https://discordapp.com/guidelines)",
            inline=False
        )

        embed.set_footer(text="Violating these rules may result in warnings, mutes, or bans. Be cool 😎")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Rules(bot))
