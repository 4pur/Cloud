import datetime
import discord

from discord.ext import commands
from discord.interactions import Interaction

i = 0

ban =       "Bans a user from the server."
unban =     "Unbans a user from the server."
kick =      "Kicks a user from the server."
mute =      "Mutes a user."
unmute =    "Unmutes a user."

warn =      "Warns a user."
warns =     "View a user's warnings"

purge =     "Purges a certain amount of messages."
lock =      "Locks a channel."
unlock =    "Unlocks a channel."
slowmode =  "Sets a channel's slowmode."
nuke =      "Delete all messages from a channel."

ticket =    "Creates an embed, with a button to create a ticket."
close =     "Closes a ticket."
add =       "Adds a user to a ticket."
remove =    "Removes a user from a ticket."

autorole = "Gives users a role upon joining the server."
role = "Gives a user a role."
removerole = "Removes a role from a user, usage: $removerole <user> <role>"

embed = "Creates a custom embed."

play = "Plays a song, usage: $play <song name>"
join = "Joins a voice channel."
stop = "Stops the music."
pause = "Pauses the music."
resume = "Resumes the music."
leave = "Leaves the voice channel."

eightball = "Ask the magic 8ball a question."
class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="help", aliases=["h"])
    async def help(self, ctx):
        e = discord.Embed(title="Help", color=0x00ff00, timestamp = datetime.datetime.now())

        e.add_field(name="Ban", value=ban, inline=False)
        e.add_field(name="Unban", value=unban, inline=False)
        e.add_field(name="Kick", value=kick, inline=False)
        await ctx.send(embed = e, view=ButtonView())
        

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
        e = discord.Embed(title="Help", color=0x00ff00, timestamp = datetime.datetime.now())

        global i
        i += 1
        
        if i > 4:
            i -= 1
        
        if i == 0:
            e.add_field(name="Ban", value=ban, inline=False)
            e.add_field(name="Unban", value=unban, inline=False)
            e.add_field(name="Kick", value=kick, inline=False)
        
        if i == 1:
            e.add_field(name="Warn", value=warn, inline=False)
            e.add_field(name="Warns", value = warns)
            e.add_field(name="Autorole", value = autorole, inline = False)
            e.add_field(name = "Role", value = role, inline = False)
            e.add_field(name = "removerole (rr)", value = removerole, inline = False)
            
        if i == 2:
            
            e.add_field(name="Purge", value=purge, inline=False)
            e.add_field(name="Lock", value=lock, inline=False)
            e.add_field(name="Unlock", value=unlock, inline=False)
            e.add_field(name="Slowmode", value=slowmode, inline=False)
            e.add_field(name="Nuke", value=nuke, inline=False)
            
        if i == 3:
            e.add_field(name="Ticket", value = ticket, inline = False)
            e.add_field(name="Close", value = close, inline = False)
            e.add_field(name="Add", value = add, inline = False)
            e.add_field(name="Remove", value = remove, inline = False)
            
        if i == 4:
            e.add_field(name="Play", value = play, inline = False)
            e.add_field(name="Join", value = join, inline = False)
            e.add_field(name="Stop", value = stop, inline = False)
            e.add_field(name="Pause", value = pause, inline = False)
            e.add_field(name="Resume", value = resume, inline = False)
            e.add_field(name="Leave", value = leave, inline = False)

        if i == 5:
            e.add_field(name="8ball", value = eightball, inline = False)
            
        await interaction.response.edit_message(embed = e, view = ButtonView())

class BackButton(discord.ui.Button):
    def __init__(self, custom_id, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_id = custom_id
        self.label = label
        
    async def callback(self, interaction: Interaction):
        global i
        i -= 1

        e = discord.Embed(title="Help", color=0x00ff00, timestamp = datetime.datetime.now())

        if i < 0:
            i += 1

        if i == 0:
            e.add_field(name="Ban", value=ban, inline=False)
            e.add_field(name="Unban", value=unban, inline=False)
            e.add_field(name="Kick", value=kick, inline=False)

        
        if i == 1:
            e.add_field(name="Warn", value=warn, inline=False)
            e.add_field(name="Warns", value = warns)
            e.add_field(name="Autorole", value = autorole, inline = False)
            e.add_field(name = "Role", value = role, inline = False)
            e.add_field(name = "removerole (rr)", value = removerole, inline = False)
            
            
        if i == 2:
            
            e.add_field(name="Purge", value=purge, inline=False)
            e.add_field(name="Lock", value=lock, inline=False)
            e.add_field(name="Unlock", value=unlock, inline=False)
            e.add_field(name="Slowmode", value=slowmode, inline=False)
            e.add_field(name="Nuke", value=nuke, inline=False)
            
        if i == 3:
            e.add_field(name="Ticket", value = ticket, inline = False)
            e.add_field(name="Close", value = close, inline = False)
            e.add_field(name="Add", value = add, inline = False)
            e.add_field(name="Remove", value = remove, inline = False)
            
        if i == 4:
            e.add_field(name="Play", value = play, inline = False)
            e.add_field(name="Join", value = join, inline = False)
            e.add_field(name="Stop", value = stop, inline = False)
            e.add_field(name="Pause", value = pause, inline = False)
            e.add_field(name="Resume", value = resume, inline = False)
            e.add_field(name="Leave", value = leave, inline = False)
            
        if i == 5:
            e.add_field(name="8ball", value = eightball, inline = False)
        
        await interaction.response.edit_message(embed = e, view = ButtonView())
        
class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(BackButton(custom_id="back", label="Previous Page"))
        self.add_item(ForwardButton(custom_id="forward", label="Next Page"))
