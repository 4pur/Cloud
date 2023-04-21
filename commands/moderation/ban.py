import discord
from discord.ext import commands

class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    # @commands.has_permissions(ban_members = True) Causing unnessecary errors, fix later.
    async def ban(ctx, m: discord.Member, r = str):
        for ms in m:
            await m.ban(reason = r)
            await ctx.send(f"Banned {m} for {r}")