import discord

from discord.ext import commands
from time import sleep

x = False

class SpamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def startspam(self, ctx):
        x = True
        while x == True:
            await ctx.send("z")
            sleep(1) # Avoid rate limits.
    
    @commands.command()
    async def stopspam(self, ctx):
        x = False
        print("Stopped spamming...")