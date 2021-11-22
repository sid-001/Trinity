from discord.ext import commands
from embeds import embed_bal
# from Mainfest import Database

class Economy(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command()
    async def bal(self, ctx):
        await ctx.reply(embed=embed_bal.bal(100000,ctx))

def setup(bot):
    bot.add_cog(Economy(bot))
# [20:18]
# not getting ctx att.