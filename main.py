from discord.ext import commands
import discord
from dotenv import load_dotenv; load_dotenv() # Read .env file contents
from os import getenv; TOKEN = getenv("TOKEN")

Cloud = commands.Bot(command_prefix='.', intents=discord.Intents(message_content = True, members = True, messages = True))

@commands.command()

@commands.has_permissions(ban_members = True)
async def ban(ctx, m: discord.Member, r = str):
    for ms in m:
        await m.ban(reason = r)

@commands.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, m: discord.Member, reason = None):
    await m.kick


@commands.add_command(ban)
@commands.add_command(kick)
Cloud.run(TOKEN)