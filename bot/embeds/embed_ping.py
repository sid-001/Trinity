import discord

def ping(latency):
    embedVar = discord.Embed(
        title="Pong!",
        description=f"**Latency** : 🟢 {latency} ms",
        color=0xFF0000,
    )
    embedVar.set_footer(
        text="Type ,help command for more info on a command. You can also type ,help category for more info on a category.")
    return embedVar
