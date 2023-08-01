from discord.ext import commands

class LogsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="logs", aliases=["log", "l"])
    async def logs(self, ctx, a, *, info):
        if a == channel:
            await ctx.send(f"Logging channel changed to {info}.")