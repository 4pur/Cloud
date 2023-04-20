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
        await ctx.send(f"Banned {m} for {r}")

@commands.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, m: discord.Member, r = str):
    for ms in m:
        await m.kick(reason = r)
        await ctx.send(f"Kicked {m} for {r}")

@commands.command()
@commands.has_permissions(moderate_members = True)
async def timeout(ctx, m: discord.Member, r = str, u = dt.utcnow()):
    for ms in m:
        await m.timeout(reason = r, until = u)
        await ctx.send(f"Timed out {m} until {u}, for {r}.")

@commands.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, m: discord.Member):
    for ms in m:
        await m.unban
        ctx.send(f"Unbanned {u}.")

Cloud.add_command(timeout)
Cloud.add_command(kick)
Cloud.add_command(ban)
Cloud.add_command(unban)
Cloud.run(TOKEN)