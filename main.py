import discord

from discord.ext import commands
from dotenv import load_dotenv; load_dotenv() # Read .env file contents
from os import getenv; TOKEN = getenv("TOKEN")

from commands.moderation.ban import BanCog
from commands.moderation.unban import UnbanCog
from commands.moderation.kick import KickCog
from commands.moderation.timeout import TimeoutCog

Cloud = commands.Bot(command_prefix='.', intents=discord.Intents(message_content = True, members = True, messages = True))
print("online!")

Cloud.add_cog(BanCog(Cloud))
Cloud.add_cog(UnbanCog(Cloud))
Cloud.add_cog(KickCog(Cloud))
Cloud.add_cog(TimeoutCog(Cloud))
Cloud.run(TOKEN)