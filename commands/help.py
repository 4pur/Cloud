import datetime
import discord

from discord.ext import commands
from discord.interactions import Interaction

i = 0

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
        e = discord.Embed(title="Help", description="Moderation Commands", color=0x00ff00, timestamp = datetime.datetime.utcnow())
        
        e.add_field(name="Ban", value="Bans a user from the server.", inline=False)
        e.add_field(name="Unban", value="Unbans a user from the server.", inline=False)
        e.add_field(name="Kick", value="Kicks a user from the server.", inline=False)
        e.add_field(name="Mute", value="Mutes a user.", inline=False)
        e.add_field(name="Unmute", value="Unmutes a user.", inline=False)

        await interaction.response.send_message(embed = e, view = ButtonView())

class MiscView(discord.ui.View):
    def __init__(self, custom_id, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_id = custom_id
        self.label = label

class ForwardButton(discord.ui.Button):
    def __init__(self, custom_id, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_id = custom_id
        self.label = label
        
    async def callback(self, interaction: discord.Interaction):
        global i
        i += 1
        
        e = discord.Embed(title="Help", description="Moderation Commands", color=0x00ff00, timestamp = datetime.datetime.utcnow())
        
        if i > 2:
            i -= 1
        
        if i == 0:
            e.add_field(name="Ban", value="Bans a user from the server.", inline=False)
            e.add_field(name="Unban", value="Unbans a user from the server.", inline=False)
            e.add_field(name="Kick", value="Kicks a user from the server.", inline=False)
            e.add_field(name="Mute", value="Mutes a user.", inline=False)
            e.add_field(name="Unmute", value="Unmutes a user.", inline=False)
        
        if i == 1:
            e.add_field(name="Warn", value="Warns a user.", inline=False)
            e.add_field(name="Unwarn", value="Unwarns a user.", inline=False)
            e.add_field(name="Warns", value = "View a user's warnings")
            
        if i == 2:
            
            e.add_field(name="Purge", value="Purges a certain amount of messages.", inline=False)
            e.add_field(name="Lock", value="Locks a channel.", inline=False)
            e.add_field(name="Unlock", value="Unlocks a channel.", inline=False)
            e.add_field(name="Slowmode", value="Sets a channel's slowmode.", inline=False)
            e.add_field(name="Nuke", value="Nukes a channel.", inline=False)
            
        if i == 3:
            e.add_field(name="Ticket", value = "Creates an embed, with a button to create a ticket, id is the category the tickets are created in.")
            e.add_field(name="Close", value = "Closes a ticket.")
            e.add_field(name="Add", value = "Adds a user to a ticket.")
            e.add_field(name="Remove", value = "Removes a user from a ticket.")
        await interaction.response.edit_message(embed = e, view = ButtonView())

class BackButton(discord.ui.Button):
    def __init__(self, custom_id, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_id = custom_id
        self.label = label
        
    async def callback(self, interaction: Interaction):
        global i
        i -= 1

        e = discord.Embed(title="Help", description="Moderation Commands", color=0x00ff00, timestamp = datetime.datetime.utcnow())

        if i < 0:
            i += 1

        if i == 0:
            e.add_field(name="Ban", value="Bans a user from the server.", inline=False)
            e.add_field(name="Unban", value="Unbans a user from the server.", inline=False)
            e.add_field(name="Kick", value="Kicks a user from the server.", inline=False)
            e.add_field(name="Mute", value="Mutes a user.", inline=False)
            e.add_field(name="Unmute", value="Unmutes a user.", inline=False)
        
        
        if i == 1:
            e.add_field(name="Warn", value="Warns a user.", inline=False)
            e.add_field(name="Unwarn", value="Unwarns a user.", inline=False)
            e.add_field(name="Warns", value = "View a user's warnings")
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

