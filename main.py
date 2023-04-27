import discord
import logging

from discord.ext import commands
from dotenv      import load_dotenv
from os          import getenv

from commands.moderation.ban import BanCog
from commands.moderation.kick import KickCog
from commands.moderation.timeout import TimeoutCog
from commands.moderation.unban import UnbanCog

from commands.misc.spam import SpamCog

from commands.util.avatar import AvatarCog
from commands.util.clear import ClearCog

from commands.ai.ask import AskCog

i = 0

# for str in ["commands.moderation.ban", "commands.moderation.unban", "commands.moderation.kick", "commands.moderation.timeout", "commands.misc.spam", "commands.util.avatar", "commands.util.clear"]:
    # i += 1
    # exec(f"from {str} import {str.split('.')[-1].capitalize()}Cog")
    
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