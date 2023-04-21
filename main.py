import discord

from discord.ext import commands
from dotenv import load_dotenv; load_dotenv() # Read .env file contents
from os import getenv; TOKEN = getenv("TOKEN")

from commands.moderation.ban import ban

Cloud = commands.Bot(command_prefix='.', intents=discord.Intents(message_content = True, members = True, messages = True))
print("online!")



@commands.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, m: discord.Member, r = str):
    for ms in m:
        await m.kick(reason = r)
        await ctx.send(f"Kicked {m} for {r}")

@commands.command()
@commands.has_permissions(moderate_members = True)
async def timeout(ctx, m: discord.Member, r = str):
    for ms in m:
        await m.timeout(reason = r)
        await ctx.send(f"Timed out {m} for {r}.")

@commands.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, m: discord.Member):
    for ms in m:
        await m.unban
        ctx.send(f"Unbanned {u}.")
        
@commands.command()
async def who(ctx):
    if ctx.author.id == 293545401972424725:
        await ctx.send(f"You are {ctx.author}")
    else:
        await ctx.send(f"I do not know you.")
        
        
Cloud.add_cog(ban(Cloud))
Cloud.run(TOKEN)