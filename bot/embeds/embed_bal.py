import discord
import datetime

def bal(userbal: int,ctx):
    embed = discord.Embed(title=f"{ctx.author.name}'s balance", color=0xFF0000)
    embed.set_thumbnail(url="https://i.imgur.com/uZIlRnK.png%22")
    embed.add_field(name=f"{userbal} Coins", value="\u200b")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="Economy")
    return embed
