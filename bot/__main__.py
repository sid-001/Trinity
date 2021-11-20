from discord.ext import commands
from discord.ext.commands import cog
from dotenv import load_dotenv
from decouple import config
from botcogs import cogs


TOKEN = config("Token")
OWNER_ID = config("Owner_id")
LOG_CHANNEL = config("Log_channel_id")
MODERATORS_ID = config("Mod_id")

client = commands.Bot(
    command_prefix='s!',
)

client.load_extension("cogs")

client.run(TOKEN)
