from discord.ext import commands
from Tools import quotes_api
from embeds import embed_quote

class Trinity(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command()
    async def quote(self, ctx):
        data = quotes_api._Quotes_()
        dataN = data._response_()
        quote = data.quote(dataN)
        author = data.author(dataN)
        # data.quote
        # data.author
        await ctx.send(embed=embed_quote.quote(quote, author=author))

def setup(bot):
    bot.add_cog(Trinity(bot))