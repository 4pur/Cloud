from discord.ext import commands

class InviteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="invite")
    async def invite(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=308291084088377344&permissions=8&scope=bot")