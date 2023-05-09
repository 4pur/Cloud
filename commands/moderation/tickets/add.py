import discord

from discord.ext import commands

class AddCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add")
    @commands.has_permissions(manage_messages=True)
    async def add(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.send("No member mentioned, try again.")
        else:
            await ctx.channel.set_permissions(member, read_messages=True, send_messages=True)
            await ctx.send("Member added to the ticket.")