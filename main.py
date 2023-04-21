import discord
import datetime as dt
import sys
sys.path.append(f'C:\\Users\\{NAME}\\Cloud\\commands\\moderation')

from discord.ext import commands
from dotenv import load_dotenv; load_dotenv() # Read .env file contents
from os import getenv; TOKEN = getenv("TOKEN"); USERNAME = getenv("NAME")

Cloud = commands.Bot(command_prefix='.', intents=discord.Intents(message_content = True, members = True, messages = True))









Cloud.add_command(timeout)
Cloud.add_command(kick)
Cloud.add_command(ban)
Cloud.add_command(unban)
Cloud.run(TOKEN)