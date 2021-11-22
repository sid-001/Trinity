from discord.ext import commands
import asyncio

class Trinity(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(brief='Clear messages')
    async def clear(self, ctx, amount=1):
        if ctx.author.id == 767758266155401226:
            try:
                await ctx.channksdel.purge(limit=amount+1)
                msg = await ctx.send(f"{ctx.message.author.mention} purged {amount} messages!")
                await asyncio.sleep(10)
                await msg.delete()
            except:
                await ctx.reply("`Manage messages` Perms missing!")
        else:
            await ctx.reply("No")
def setup(bot):
    bot.add_cog(Trinity(bot))