import discord
from discord import embeds


class Trinity_Embeds:
    def ping(self, latency):
        embedVar = discord.Embed(
            title="Pong!",
            description=f"**Latency** : 🟢 {latency} ms",
            color=0xFF0000,
        )
        embedVar.set_footer(
            text="Type ,help command for more info on a command. You can also type ,help category for more info on a category.")
        return embedVar

    def servers(self, lists, namestr, countstr):
        embedVar = discord.Embed(
            title=f"Servers connected! : {len(lists)}",
            color=0xFF0000,
        )

        embedVar.add_field(
            name="Servers",
            value=namestr,
            inline=True,
        )
        embedVar.add_field(
            name="Member count",
            value=countstr,
            inline=True,
        )
        embedVar.set_footer(
            text="Type ,help command for more info on a command. You can also type ,help category for more info on a category.")
        return embedVar
