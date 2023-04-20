from discord.ext import commands
import discord
from dotenv import load_dotenv; load_dotenv() # Read .env file contents
from os import getenv; TOKEN = getenv("TOKEN")

Cloud = commands.Bot(command_prefix='.', intents=discord.Intents(message_content = True, members = True, messages = True))

@commands.command()
async def i(ctx):
    print("a")

Cloud.add_command(i)
Cloud.run(TOKEN)