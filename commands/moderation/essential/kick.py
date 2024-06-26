"""
Kicks a member from the server

Usage: $kick @member
"""

import discord
from discord.ext import commands

class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_guild_permissions(moderate_members = True)
    async def kick(self, ctx, m: discord.Member, *, r = str):
        if m == None:
            ctx.send("You did not provide a user to kick.")
        else:
            await m.kick(reason = r)
            await ctx.send(f"Kicked {m} for {r}")
