import discord
from discord.ext import commands

x = False

class SpamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def startspam(self, ctx):
        x = True
        while x == True:
            await ctx.send("z")
    
    @commands.command()
    async def stopspam(self, ctx):
        x = False