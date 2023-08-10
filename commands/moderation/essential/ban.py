"""
Bans a member from the server

Usage: $ban @member or member id
"""

import discord
from discord.ext import commands

class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_guild_permissions(moderate_members = True)
    async def ban(self, ctx, m: discord.Member = None, *, r: str):
        if m == None:
            ctx.send("You did not provide a user to ban.")
        else:
            await m.ban(reason = r)
            await ctx.send(f"Banned {m} for {r}")
