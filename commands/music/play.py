import discord
import os
import yt_dlp as youtube_dl

from dotenv import load_dotenv
from discord.ext import commands,tasks
from commands.util.ytdl import YTDLSource

discord.opus.load_opus('util/libopus.so.0.9.0')
    
class PlayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play', aliases = ["p"])
    async def play(self, ctx, *, url):
        if self.bot.voice_clients == []:
            if not ctx.message.author.voice:
                await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
                return
            else:
                channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            pass
        
        server = ctx.message.guild
        voice_channel = server.voice_client

        #if not discord.opus.is_loaded():
            #raise RuntimeError('Failed to load Opus!')
        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=self.bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="util/ffmpeg", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))

    @commands.command(name='pause')
    async def pause(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")
        
    @commands.command(name='resume')
    async def resume(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await ctx.send("The bot was not playing anything before this. Use play_song command")

    @commands.command(name='stop')
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything at the moment.")
