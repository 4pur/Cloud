import discord
from discord.ext import commands
class UnbanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    # @commands.has_guild_permissions(moderate_members = True)
    async def unban(self, ctx, m: discord.Member, r = str):
        if m == None:
            ctx.send("You did not provide a user to unban.")

        await m.unban()
        await ctx.send(f"Unbanned {m}.")
        

            