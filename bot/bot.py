# Imported the required Modules 

import discord
import os
from discord.ext import commands
from decouple import config

#Getting  token through .env
TOKEN = config("Token")

# Intents
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="s!", intents = intents)

#-----------------------------------------------  Loading cogs   --------------------------------------------------------------------
if __name__ == '__main__':
    for filename in os.listdir("Cogs"):
        if filename.endswith(".py"):
           bot.load_extension(f"Cogs.{filename[:-3]}")

#--------------------------------------------------  Methods        ------------------------------------------------------------------
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"s!help"))

bot.run(TOKEN)