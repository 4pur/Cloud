"""
Closes a ticket, must be a ticket channel

Usage: $close
"""

import discord
import time

from discord.ext import commands

class CloseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="close", aliases=["c"])
    @commands.has_permissions(manage_messages=True)
    async def close(self, ctx):
        if ctx.channel.name.startswith("ticket-") == False:
            await ctx.send("This is not a ticket channel.")
        else:
            e = discord.Embed(title="Ticket Closed", description="The ticket has been closed by a moderator.", color=0xff0000)
            await ctx.channel.send(embed=e)
            time.sleep(3)
            await ctx.channel.delete()
