## TODO ## 
# - Add a command to change the prefix
# - Add a whois command
# - Add a help command (maybe)


import discord
import logging

from discord.ext import commands
from dotenv      import load_dotenv
from os          import getenv

i = 0

for str in ["commands.moderation.ban", "commands.moderation.unban", "commands.moderation.kick", "commands.moderation.timeout", "commands.misc.spam", "commands.util.avatar", "commands.util.clear", "commands.ai.ask"]:
    i += 1
    exec(f"from {str} import {str.split('.')[-1].capitalize()}Cog")
    
print(f"loaded {i} cogs")    

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

Cloud = commands.Bot(command_prefix='$', intents=intent)

for cog in [BanCog, UnbanCog, KickCog, TimeoutCog, SpamCog, AvatarCog, ClearCog]:
    Cloud.add_cog(cog(Cloud))

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv(); TOKEN = getenv("TOKEN")
Cloud.run(TOKEN)