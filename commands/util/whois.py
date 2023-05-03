import discord
import datetime

from discord.ext import commands


class WhoisCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="whois", aliases=["who"])
    async def whois(self, ctx, m: discord.Member = None):
        e = discord.Embed(
            title = f"{m}",
            description="wip command",
            color=0x00ff00,
            timestamp=datetime.datetime.utcnow()
        )
        
        e.add_field(name="ID", value=f"{m.id}", inline=False)
        e.add_field(name="Created at", value=f"{m.created_at}", inline=False)
        e.add_field(name="Joined at", value=f"{m.joined_at}", inline=False)
        e.add_field(name="Bot?", value=f"{m.bot}", inline=False)
        
        await ctx.send(embed=e)