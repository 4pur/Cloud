from discord.ext import commands

class SnipeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.bot.snipes[message.channel.id] = message
        
    @commands.command(name="snipe", aliases=["s"])
    async def snipe(self, ctx):
        try:
            snipe = self.bot.snipes[ctx.channel.id]
        except KeyError:
            await ctx.send("There is nothing to snipe.")
        else:
            await ctx.send(f"{snipe.author.mention} said {snipe.content}")