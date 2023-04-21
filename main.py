import discord

from discord.ext import commands
from dotenv      import load_dotenv
from os          import getenv

from commands.moderation.ban     import BanCog
from commands.moderation.unban   import UnbanCog
from commands.moderation.kick    import KickCog
from commands.moderation.timeout import TimeoutCog

from commands.ai.ask             import AskCog

Cloud = commands.Bot(command_prefix='$', intents=discord.Intents(message_content = True, members = True, messages = True))
print("online!")

# make a loop to do this for every cog imported
for cog in [BanCog, UnbanCog, KickCog, TimeoutCog, AskCog]:
    Cloud.add_cog(cog(Cloud))


load_dotenv()
TOKEN = getenv("TOKEN")
Cloud.run(TOKEN)