import discord

from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="help", aliases=["a"])
    async def help(self, ctx):
        await ctx.send(view=View())
        
class View(discord.ui.view):
    
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
        
        await interaction.response.send_message(embed = e)