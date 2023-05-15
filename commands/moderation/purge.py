import discord

from discord.ext import commands

class PurgeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, *, x: int):
        async for m in ctx.channel.history(limit = x):
            await m.delete()
        await ctx.send(f"Purged {x} messages.")
