import discord

from discord.ext import commands

class PurgeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "purge")
    @commands.has_guild_permissions(moderate_members = True)
    async def purge(self, ctx, *, x: int):
        for i in range(x):
            return