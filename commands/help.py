# being rewrote
import discord

from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="help")
    async def help(self, ctx):
        await ctx.send(view = View())
    
class SelectView(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="AI", description="AI commands"),
            discord.SelectOption(label="Economy", description="Economy commands"),
            discord.SelectOption(label="Moderation", description="Essential Moderation commands"),
            discord.SelectOption(label="Music", description="Music commands"),
            discord.SelectOption(label="Utility", description="Utility commands"),
        ]
        super().__init__(placeholder = "Select an option", max_values = 1, min_values = 1, options = options)
        
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "AI":
            embed = discord.Embed(title="AI Commands")
            embed.add_field(name="chat", value="chat with the bot")
            await interaction.response.edit_message(embed=embed)
        elif self.values[0] == "Economy":
            embed = discord.Embed(title="Economy Commands", description="Economy Commands")
            embed.add_field(name="balance", value="check your balance")
            embed.add_field(name="beg", value="beg for money")
            embed.add_field(name="deposit", value="deposit money")
            embed.add_field(name="give", value="give money to someone")
            embed.add_field(name="rob", value="rob money from someone")
            embed.add_field(name="shop", value="shop for items")
            embed.add_field(name="withdraw", value="withdraw money")
            await interaction.response.edit_message(embed=embed)
        elif self.values[0] == "Moderation":
            embed = discord.Embed(title="Moderation Commands")
            embed.add_field(name="ban", value="ban a member")
            embed.add_field(name="kick", value="kick a member")
            embed.add_field(name="mute", value="mute a member")
            embed.add_field(name="unban", value="unban a member")
            embed.add_field(name="unmute", value="unmute a member")
            embed.add_field(name="warn", value="warn a member")
            embed.add_field(name="warns", value="view a member's warnings")
            embed.add_field(name="clearwarns", value="softclear messages")
            embed.add_field(name="purge", value="delete a number of messages")
            embed.add_field(name="slowmode", value="set the slowmode of a channel")
            embed.add_field(name="lock", value="lock a channel")
            embed.add_field(name="unlock", value="unlock a channel")
            embed.add_field(name="nuke", value="clear ALL messages in a channel.")
            embed.add_field(name="addrole", value="add a role to a member")
            embed.add_field(name="removerole", value="remove a role from a member")
            embed.add_field(name="setprefix", value="set the server's prefix")
            embed.add_field(name="autorole", value="set a role to be given to new members")
            embed.add_field(name = "ticket", value = "create a ticket message")
            embed.add_field(name = "close", value = "close a ticket")
            embed.add_field(name = "add", value = "add a member to a ticket")
            embed.add_field(name = "remove", value = "remove a member from a ticket")
            await interaction.response.edit_message(embed=embed)
        elif self.values[0] == "Music":
            embed = discord.Embed(title="Music Commands")
            embed.add_field(name="join", value="join a voice channel")
            embed.add_field(name="leave", value="leave a voice channel")
            embed.add_field(name="pause", value="pause music")
            embed.add_field(name="play", value="play music")
            embed.add_field(name="queue", value="view the queue")
            embed.add_field(name="remove", value="remove a song from the queue")
            embed.add_field(name="resume", value="resume music")
            embed.add_field(name="skip", value="skip a song")
            embed.add_field(name="stop", value="stop music")
            await interaction.response.edit_message(embed=embed)
        elif self.values[0] == "Utility":
            embed = discord.Embed(title="Utility Commands")
            embed.add_field(name="avatar", value="view someone's avatar")
            embed.add_field(name="help", value="view the help menu")
            embed.add_field(name="invite", value="invite the bot to your server")
            embed.add_field(name="ping", value="view the bot's latency")
            embed.add_field(name="whois", value="view a user's information")
            await interaction.response.edit_message(embed=embed)
            
class View(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SelectView())