import discord
import sys

from discord.ext import commands
from time import sleep


x = 0

class SpamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        
    @commands.command()
    async def startspam(self, ctx):
        x = 1
        
        while x == 1:
            await ctx.send("z")
            sleep(1) # Avoid rate limits.
            
                
    @commands.command()
    async def stopspam(self, ctx):
        x = 0
        await ctx.send("Stopped spamming.")