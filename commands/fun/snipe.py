from discord.ext import commands

class SnipeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        print(f"Message deleted: {message.content}")