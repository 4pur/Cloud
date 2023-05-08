from discord.ext import commands
from time import sleep

class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="clear", aliases=["softclear", "clearmessages", "clearmsgs", "sc"])
    async def Clear(self, ctx):
        await ctx.send("clearing messages...")
        await ctx.send("‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n‎\n")