import discord

from discord.ext import commands
from dotenv      import load_dotenv
from os          import getenv

for str in ["commands.moderation.ban", "commands.moderation.unban", "commands.moderation.kick", "commands.moderation.timeout", "commands.ai.ask"]:
    exec(f"from {str} import {str.split('.')[-1].capitalize()}Cog")
    print(f"imported {str}")

Cloud = commands.Bot(command_prefix='$', intents=discord.Intents(message_content = True, members = True, messages = True))
print("online!")

# make a loop to do this for every cog imported
for cog in [BanCog, UnbanCog, KickCog, TimeoutCog, AskCog]:
    Cloud.add_cog(cog(Cloud))

load_dotenv()
TOKEN = getenv("TOKEN")
Cloud.run(TOKEN)