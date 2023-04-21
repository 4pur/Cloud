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

#
Cloud.add_cog(BanCog(Cloud))
Cloud.add_cog(UnbanCog(Cloud))
Cloud.add_cog(KickCog(Cloud))
Cloud.add_cog(TimeoutCog(Cloud))

# AI
Cloud.add_cog(AskCog(Cloud))

load_dotenv()
TOKEN = getenv("TOKEN")
Cloud.run(TOKEN)