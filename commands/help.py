import discord
from discord.ext import commands

class HelpCog(commands.Cog):
        def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    # @commands.has_permissions(moderate_members = True) Causing unnessecary errors, fix later.
    async def timeout(ctx, m: discord.Member, r = str):
        for ms in m:
            await m.timeout(reason = r)
            await ctx.send(f"Timed out {m} for {r}.")