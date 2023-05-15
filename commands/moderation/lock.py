import discord

from discord.ext import commands

class LockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command(name="lock", aliases=["lockchannel", "lockdown", "lockdownchannel", "lockc"])
    @commands.has_permissions(manage_messages=True)
    async def lock(self, ctx):
        if ctx.channel.overwrites_for(ctx.guild.default_role).send_messages == False:
            await ctx.send("This channel is already locked.")
        else:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)
            await ctx.send("Channel locked.")
            
    @commands.command(name="unlock", aliases=["unlockchannel", "unlockc"])
    @commands.has_permissions(manage_messages=True)
    async def unlock(self, ctx):
        if ctx.channel.overwrites_for(ctx.guild.default_role).send_messages == True:
            await ctx.send("This channel is not locked.")
        else:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)
            await ctx.send("Channel unlocked.")
