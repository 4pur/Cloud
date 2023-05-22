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
            embed = discord.Embed(title="AI Commands", description="AI Commands", color=0x00ff00)
            embed.add_field(name="AI", value="`talk` - Talk to me!\n`chat` - Chat with me!\n`ai` - AI commands")
            await interaction.response.send_message(embed=embed, view=SelectView())
        elif self.values[0] == "Economy":
            embed = discord.Embed(title="Economy Commands", description="Economy Commands", color=0x00ff00)
            embed.add_field(name="Economy", value="`balance` - Check your balance!\n`beg` - Beg for money!\n`give` - Give someone money!\n`rob` - Rob someone!\n`work` - Work for money!\n`economy` - Economy commands")
            await interaction.response.send_message(embed=embed, view=SelectView())
        elif self.values[0] == "Moderation":
            embed = discord.Embed(title="Moderation Commands", description="Moderation Commands", color=0x00ff00)
            embed.add_field(name="Moderation", value="`ban` - Ban someone!\n`kick` - Kick someone!\n`clear` - Clear messages!\n`mute` - Mute someone!\n`unmute` - Unmute someone!\n`moderation` - Moderation commands")
            await interaction.response.send_message(embed=embed, view=SelectView())
        elif self.values[0] == "Music":
            embed = discord.Embed(title="Music Commands", description="Music Commands", color=0x00ff00)
            embed.add_field(name="Music", value="`join` - Join a voice channel!\n`leave` - Leave a voice channel!\n`play` - Play a song!\n`pause` - Pause a song!\n`resume` - Resume a song!\n`stop` - Stop a song!\n`queue` - See the queue!\n`skip` - Skip a song!\n`music` - Music commands")
            await interaction.response.send_message(embed=embed, view=SelectView())
        elif self.values[0] == "Utility":
            embed = discord.Embed(title="Utility Commands", description="Utility Commands", color=0x00ff00)
            embed.add_field(name="Utility", value="`ping` - Check my ping!\n`help` - See this message!\n`invite` - Invite me!\n`utility` - Utility commands")
            await interaction.response.send_message(embed=embed, view=SelectView())

class View(discord.ui.View):
    def __init__(self):
        
        super().__init__()
        self.add_item(SelectView())
        