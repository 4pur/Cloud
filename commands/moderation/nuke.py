from discord.ext import commands

class NukeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="nuke", aliases=["destroy", "obliterate"])
    @commands.has_permissions(manage_messages=True)
    async def nuke(self, ctx):
        await ctx.send("Nuking channel...")
        await ctx.channel.clone()
        await ctx.channel.delete()
        await ctx.send("Channel nuked.")
