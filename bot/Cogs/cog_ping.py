from discord.ext import commands
from embeds import embed_ping



class Trinity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(embed=embed_ping.ping(round(self.bot.latency*1000, 1)))

def setup(bot):
    bot.add_cog(Trinity(bot))