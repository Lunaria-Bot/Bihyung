import discord
from discord.ext import commands

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rules")
    async def show_rules(self, ctx):
        embed = discord.Embed(
            title="📜 Server Rules",
            description=(
                "1️⃣ No obscene or explicit content.\n"
                "2️⃣ Treat everyone with respect.\n"
                "3️⃣ Harassment, bullying or any kind of hate speech will not be tolerated.\n"
                "4️⃣ No sensitive topics like race, religion, politics, etc.\n"
                "5️⃣ Use the appropriate channel to discuss topics.\n"
                "6️⃣ Advertising without explicit permission is not allowed — including through DMs.\n"
                "7️⃣ Refrain from engaging in drama or arguments — take it to DMs.\n"
                "8️⃣ Speak English so we can all understand each other.\n"
                "9️⃣ No NSFW content.\n"
                "🔟 Lastly, follow [Discord's Community Guidelines](https://discordapp.com/guidelines)."
            ),
            color=discord.Color.red()
        )
        embed.set_footer(text="Violation of these rules may result in warnings or bans.")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Rules(bot))
