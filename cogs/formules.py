import discord
from discord.ext import commands

class Formules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="formules")
    async def show_formules(self, ctx):
        embeds = []

        # Classic Bot Mazoku
        embed_classic = discord.Embed(
            title="💼 Classic Bot Mazoku",
            description=(
                "💰 **Price**: 5 $ / month or 100k <:Bloodstone:1438158173017084047>\n"
                "<a:white_arrow:1438158066028777523> Access to <@1421115186844143746> for a month\n"
                "<a:white_arrow:1438158066028777523> Access to frame testing\n"
                "<a:white_arrow:1438158066028777523> High tier ping config\n"
                "<a:white_arrow:1438158066028777523> Daily Reminder\n"
                "<a:white_arrow:1438158066028777523> Vote Reminder\n"
                "<a:white_arrow:1438158066028777523> Event cooldowns"
            ),
            color=discord.Color.blue()
        )
        embeds.append(embed_classic)

        # Custom Mazoku Bot
        embed_custom = discord.Embed(
            title="🛠️ Custom Mazoku Bot",
            description=(
                "<a:white_arrow:1438158066028777523> **Price**: Build price + 150k <:Bloodstone:1438158173017084047> or 7.5 $ / month\n"
                "<a:white_arrow:1438158066028777523> Access to your bot for 2 months\n"
                "<a:white_arrow:1438158066028777523> Adding features available in [this channel](https://discord.com/channels/1437641569187659928/1438154858355232829)\n"
                "<a:white_arrow:1438158066028777523> Priority on new functionality updates added by Mazoku"
            ),
            color=discord.Color.orange()
        )
        embeds.append(embed_custom)

        # General Bot
        embed_general = discord.Embed(
            title="📦 Other Types of General Bots",
            description=(
                "<a:white_arrow:1438158066028777523> **Price**: 5 $ / month or 100k <:Bloodstone:1438158173017084047>\n"
                "<a:white_arrow:1438158066028777523> Access to your bot for a month\n"
                "<a:white_arrow:1438158066028777523> Features can be added via [this channel](https://discord.com/channels/1437641569187659928/1438154858355232829)"
            ),
            color=discord.Color.purple()
        )
        embeds.append(embed_general)

        for embed in embeds:
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Formules(bot))
