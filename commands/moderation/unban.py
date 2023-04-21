import discord
from discord.ext import commands

class UnbanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(ctx, m: discord.Member, r = str):
        for ms in m:
            await m.unban()
            await ctx.send(f"Unbanned {m}.")