import discord
import datetime


def quote(Quote, author=None):
    embedVar = discord.Embed(title="Quote", description=Quote, color=0x000ff00)
    embedVar.set_footer(text=f"Quote by {author}")
    embedVar.timestamp = datetime.datetime.utcnow()
    return embedVar
