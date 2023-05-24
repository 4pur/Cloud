from discord.ext import commands

class TimestampCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="timestamp", aliases=["ts"])
    async def timestamp(self, ctx):
        await ctx.send(f"The current timestamp is {ctx.message.created_at}.")