import discord

from discord.ext import commands

class CwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="clearwarn", aliases=["cw", "clearwarns", "cws"])
    @commands.has_permissions(manage_messages=True)
    async def clearwarn(self, ctx, member: discord.Member):
        with open(f'warns/{member.id}.csv', 'w') as w:
            w.write("")
        await ctx.send(f"Cleared warnings for {member.mention}.")