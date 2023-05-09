import discord
from discord.ext import commands

class TimeoutCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_guild_permissions(moderate_members = True)
    async def timeout(self, ctx, m: discord.Member, r = str):
        if m == None:
            ctx.send("You did not provide a user to timeout.")

        await m.timeout(reason = r, until=0)
        await ctx.send(f"Timed out {m} for {r}.")