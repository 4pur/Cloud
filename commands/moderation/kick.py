import discord
from discord.ext import commands

class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    # @commands.has_guild_permissions(moderate_members = True)
    async def kick(self, ctx, m: discord.Member, r = str):
        await m.kick(reason = r)
        await ctx.send(f"Kicked {m} for {r}")