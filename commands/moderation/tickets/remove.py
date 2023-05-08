import discord

from discord.ext import commands

class RemoveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="remove", aliases=["r"])
    @commands.has_permissions(manage_messages=True)
    async def remove(self, ctx, member: discord.Member = None):
        if ctx.channel.name != "ticket-{}".format(ctx.author):
            await ctx.send("This is not a ticket channel.")
        else:
            if member == None:
                await ctx.send("No member mentioned, try again.")
            else:
                await ctx.channel.set_permissions(member, read_messages=False, send_messages=False)
                await ctx.send("Member removed from the ticket.")