import discord
from discord import Embed
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def help(ctx, m: discord.Member):
        ctx.send(Embed(title="test"))