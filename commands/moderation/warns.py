import csv
import discord

from discord.ext import commands

class WarnsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="warns", aliases=["ws"])
    @commands.has_permissions(manage_messages=True)
    async def warns(self, ctx, member: discord.Member):
        with open(f'warns/{member.id}.csv', 'r') as w:
            await ctx.send(w.read())