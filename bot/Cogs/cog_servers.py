from discord.ext import commands
from embeds import embed_servers
import asyncio
class Trinity(commands.Cog):

    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def servers(self, ctx):
        if ctx.message.author.id in [858195823296905256, 767758266155401226]:
            lists, index = [], 1
            for server in self.bot.guilds:
                lists.append((server.name, server.member_count))
            _nameStr, _countStr = "", ""

            for name, count in lists:
                _nameStr += f"{index}. {name}\n"
                _countStr += f"{str(count)}\n"
                index += 1
            msg = await ctx.reply(embed=embed_servers.Servers(lists=lists, namestr=_nameStr, countstr=_countStr))
            await asyncio.sleep(15)
            await msg.edit(content="You Baka! Sus")
            await msg.delete()


def setup(bot):
    bot.add_cog(Trinity(bot))
