from discord.ext import commands
import discord
import datetime as dt
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
async def kick(ctx, m: discord.Member, r = str):
    for ms in m:
        await m.kick(reason = r)
        await ctx.send(f"Kicked {m} for {r}")

@commands.command()
@commands.has_permissions(moderate_members = True)
async def timeout(ctx, m: discord.Member, r = str, u = str):
    for ms in m:
        await m.timeout(reason = r, until = dt.utcnow())

@commands.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, m: discord.Member):
    for ms in m:
        await m.unban

Cloud.add_command(ban)
Cloud.add_command(kick)
Cloud.run(TOKEN)