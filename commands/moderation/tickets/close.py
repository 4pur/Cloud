import discord

from discord.ext import commands

class CloseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="close", aliases=["c"])
    @commands.has_permissions(manage_messages=True)
    async def close(self, ctx):
        e = discord.Embed(title="Ticket Closed", description="The ticket has been closed by a moderator.", color=0xff0000)
        await ctx.channel.send(embed=e)
        await ctx.channel.set_permissions(ctx.author, read_messages=False, send_messages=False)
        if ctx.channel.name != "ticket-{}".format(ctx.author):
            await ctx.send("This is not a ticket channel.")
        
        await ctx.channel.delete()