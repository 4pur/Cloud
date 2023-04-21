import discord
from discord.ext import commands

class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def kick(ctx, m: discord.Member, r = str):
        for ms in m:
            await m.kick(reason = r)
            await ctx.send(f"Kicked {m} for {r}")