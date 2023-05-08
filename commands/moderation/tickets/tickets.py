import discord

from discord.ext import commands

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ticket", aliases=["t"])
    @commands.has_permissions(manage_messages=True)
    async def ticket(self, ctx):
        await ctx.send(view=CreateView())
        
class CreateView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        
    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.green)
    async def create(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Ticket created!", ephemeral=True)
        await interaction.message.delete()
        
        channel = await interaction.guild.create_text_channel(f"ticket-{interaction.user.name}", category=interaction.channel.category)
        await channel.set_permissions(interaction.guild.default_role, read_messages=False)
        await channel.set_permissions(interaction.user, read_messages=True)
        
        e = discord.Embed(title="Ticket", description="Ticket created!", color=0x00ff00)
        e.add_field(name="Channel", value=channel.mention)
        e.add_field(name="User", value=interaction.user.mention)
        
        await interaction.user.send(embed=e)
        
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Ticket cancelled!", ephemeral=True)
        await interaction.message.delete()