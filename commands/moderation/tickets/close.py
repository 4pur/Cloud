import discord

from discord.ext import commands

class CloseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="close", aliases=["c"])
    @commands.has_permissions(manage_messages=True)
    async def close(self, ctx):
        
        if ctx.channel.name.startswith("ticket-"):
            await ctx.send("Ticket closed!")
            await ctx.channel.delete()
            
        else:
            await ctx.send("This is not a ticket channel!")