from discord.ext import commands
from time import sleep

class AvatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="avatar", aliases=["av", "pfp"])
    async def get(self, ctx, user: commands.UserConverter = None):
        if user == None:
            user = ctx.author
        await ctx.send(user.avatar)