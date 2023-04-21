import discord
from discord import Embed
from discord.ext import commands

e = Embed(color=(0xeca4fb), title="Help")

e.add_field(name="test", 
            value="test2",
            inline=False)

class xCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context = True)
    async def x(ctx, c):
        await ctx.send(embed=e)
        print(c)