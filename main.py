import discord

from discord.ext import commands
from dotenv      import load_dotenv
from os          import getenv



Cloud = commands.Bot(command_prefix='.', intents=discord.Intents(message_content = True, members = True, messages = True))
print("online!")



load_dotenv()
TOKEN = getenv("TOKEN")
Cloud.run(TOKEN)