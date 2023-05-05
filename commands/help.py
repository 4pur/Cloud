import discord

from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="help", aliases=["a"])
    async def help(self, ctx):
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
    
    async def callback(self, select, interaction: discord.Interaction):
        e = discord.Embed(title="Help", description="Moderation Commands", color=0x00ff00)
        e.add_field(name="Ban", value="Bans a user from the server.", inline=False)
        e.add_field(name="Unban", value="Unbans a user from the server.", inline=False)
        e.add_field(name="Kick", value="Kicks a user from the server.", inline=False)
        e.add_field(name="Mute", value="Mutes a user.", inline=False)
        e.add_field(name="Unmute", value="Unmutes a user.", inline=False)
        
        await interaction.response.send_message(embed = e, view = ButtonView())
        
class ButtonView(discord.ui.View):
    @discord.ui.button(
        label="",
        style=discord.ButtonStyle.primary,
        row = 1,
        emoji="⬅️"
    )
    

    
    async def button_callback(self, button, interaction):
        return

class DefaultButton(discord.ui.Button):
    def __init__(self, custom_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_id = custom_id
        
ButtonView.