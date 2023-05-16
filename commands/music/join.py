import discord

from discord.ext import commands

class JoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = "join")
    async def Join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(name = "leave")
    async def Leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")