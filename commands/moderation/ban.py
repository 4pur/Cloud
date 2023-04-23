import discord
from discord.ext import commands

class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    # @commands.has_guild_permissions(moderate_members = True)
    async def ban(self, ctx, m: discord.Member, r = str):
        await m.ban(reason = r)
        await ctx.send(f"Banned {m} for {r}")