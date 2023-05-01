import discord

from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="help")
    def help(self, ctx):
        return