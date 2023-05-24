from discord.ext import commands

class ListCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="list", aliases=["l"])
    async def list(self, ctx, *, name: str):
        i = 0
        for member in ctx.guild.members:
            if member.name == name:
                i += 1
        await ctx.send(f"There are {i} members with the name {name}.")