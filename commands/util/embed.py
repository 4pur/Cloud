import discord

from discord.ext import commands

class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="embed")
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx, title, *, desc):
        e = discord.Embed(title = title)
        e.add_field(desc)
        
        ctx.send(embed = e)
