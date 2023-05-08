# idfk why it doesnt work

import discord

from discord.ext import commands
from discord.interactions import Interaction

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="help", aliases=["a"])
    async def help(self, ctx):
        global ctx1 
        ctx1 = ctx
        await ctx.send(view=SelectView())
        
class SelectView(discord.ui.View):
    
    @discord.ui.select(
        placeholder = "Select a category",
        min_values = 1,
        max_values = 1,
        options = [
        discord.SelectOption(
            label="Moderation",
            description="Moderation commands."
        )])
    
    async def callback(self, x, interaction: discord.Interaction):
        e = discord.Embed(title="Help", description="Moderation Commands", color=0x00ff00)
        
        e.add_field(name="Ban", value="Bans a user from the server.", inline=False)
        e.add_field(name="Unban", value="Unbans a user from the server.", inline=False)
        e.add_field(name="Kick", value="Kicks a user from the server.", inline=False)
        e.add_field(name="Mute", value="Mutes a user.", inline=False)
        e.add_field(name="Unmute", value="Unmutes a user.", inline=False)
        
        await ctx1.send("Page 1/3")
        await interaction.response.send_message(embed = e, view = ButtonView())


i = 0

class ForwardButton(discord.ui.Button):
    def __init__(self, custom_id, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_id = custom_id
        self.label = label
        
    async def callback(self, x, interaction: discord.Interaction):
        await ctx1.delete()
        
        i += 1
        
        e = discord.Embed(title="Help", description="Moderation Commands", color=0x00ff00)
        
        if i == 1:
            e.add_field(name="Warn", value="Warns a user.", inline=False)
            e.add_field(name="Unwarn", value="Unwarns a user.", inline=False)
            e.add_field(name="warns", value="Shows a user's warns.", inline=False)
            
        if i == 2:
            
            e.add_field(name="Purge", value="Purges a certain amount of messages.", inline=False)
            e.add_field(name="Lock", value="Locks a channel.", inline=False)
            e.add_field(name="Unlock", value="Unlocks a channel.", inline=False)
            e.add_field(name="Slowmode", value="Sets a channel's slowmode.", inline=False)
            e.add_field(name="Nuke", value="Nukes a channel.", inline=False)
            
        await interaction.response.edit_message(embed = e, view = ButtonView())

class BackButton(discord.ui.Button):
    def __init__(self, custom_id, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_id = custom_id
        self.label = label
        
    async def callback(self, x, interaction: Interaction):
        await ctx1.delete()
        
        if i == 0:
            return
        
        i -= 1
        
        e = discord.Embed(title="Help", description="Moderation Commands", color=0x00ff00)
        
        if i == 1:
            e.add_field(name="Warn", value="Warns a user.", inline=False)
            e.add_field(name="Unwarn", value="Unwarns a user.", inline=False)
            e.add_field(name="Warns", value="Shows a user's warns.", inline=False)
            
        if i == 2:
            
            e.add_field(name="Purge", value="Purges a certain amount of messages.", inline=False)
            e.add_field(name="Lock", value="Locks a channel.", inline=False)
            e.add_field(name="Unlock", value="Unlocks a channel.", inline=False)
            e.add_field(name="Slowmode", value="Sets a channel's slowmode.", inline=False)
            e.add_field(name="Nuke", value="Nukes a channel.", inline=False)
        
        await interaction.response.edit_message(embed = e, view = ButtonView())
        
class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(BackButton(custom_id="back", label="Previous Page"))
        self.add_item(ForwardButton(custom_id="forward", label="Next Page"))