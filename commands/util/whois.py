import discord

from discord.ext import commands

class WhoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="whois", aliases=["who"])
    async def whois(self, ctx, m: discord.Member = None):
        await ctx.send("This command is a wip.")
        
        await ctx.send(f"Created at: {m.created_at}")
        await ctx.send(f"Joined at: {m.joined_at}")
        await ctx.send(f"Roles: {m.roles}")
        await ctx.send(f"Name: {m.name}+{str(m.discriminator)}")
        await ctx.send(f"ID: {m.id}")
        await ctx.send(f"Avatar: {m.avatar}")