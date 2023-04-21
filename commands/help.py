import discord
from discord import Embed
from discord.ext import commands

e = Embed(
    color=(0xeca4fb),
    title="Help")
e.add_field("test")

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def help(ctx, m: discord.Member):
        await ctx.send(e)