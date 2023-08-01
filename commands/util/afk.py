from discord.ext import commands

class AfkCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="afk")
    async def afk(self, ctx):
        await ctx.send(f"{ctx.author.mention} is now AFK.")
        await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if message.author.nick and message.author.nick.startswith("[AFK]"):
            await message.author.edit(nick=message.author.nick.replace("[AFK] ", ""))
            await message.channel.send(f"Welcome back {message.author.mention}, I removed your AFK status.")
            
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if message.mentions:
            for user in message.mentions:
                if user.nick and user.nick.startswith("[AFK]"):
                    await message.channel.send(f"{user.display_name} is AFK.")
                else:
                    pass