import discord

from datetime import datetime
from discord.ext import commands

class WarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="warn", aliases=["w"])
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = "No reason provided."
        await member.send(f"You have been warned in {ctx.guild.name} for {reason}.")
        await ctx.send(f"{member.mention} has been warned for {reason}.")
        await ctx.message.delete()

        with open(f'warns/{member.id}.csv', 'a') as w:
            w.write(f"Warned for {reason}, on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S UTC')}\n")