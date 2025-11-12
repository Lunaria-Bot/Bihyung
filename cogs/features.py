import discord
from discord.ext import commands

class Features(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="features")
    async def show_features(self, ctx):
        embed = discord.Embed(
            title="🛠️ Mazoku Bot Custom Features",
            description="Here are the current features available for Mazoku Bot Custom",
            color=discord.Color.dark_purple()
        )

        embed.add_field(
            name="✨ Features",
            value=(
                "<a:white_arrow:1438158066028777523> High Tier ping \n"
                "<a:white_arrow:1438158066028777523> Summon Reminder \n"
                "<a:white_arrow:1438158066028777523> Vote/Daily Reminder\n"
                "<a:white_arrow:1438158066028777523> Frame Testing\n"
                "<a:white_arrow:1438158066028777523> Auction System\n"
                "<a:white_arrow:1438158066028777523> Shop System + Currency System\n"
                "<a:white_arrow:1438158066028777523> Market System\n"
                "<a:white_arrow:1438158066028777523> Quest System"
            ),
            inline=False
        )

        embed.set_footer(text="Mazoku Bot • Features evolve regularly 🚀")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Features(bot))
