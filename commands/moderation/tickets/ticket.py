import discord

from discord.ext import commands
from discord.ui.input_text import InputText

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ticket", aliases=["t"])
    @commands.has_permissions(manage_messages=True)
    async def ticket(self, ctx):
        await ctx.send(view=TicketPromptView())
        
class TicketPromptView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(label="Create Ticket Embed", custom_id="create_ticket_embed", style=discord.ButtonStyle.green))
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(CreateTicketPromptModal(title="Create Ticket Embed", description="Please enter the ticket categor(ies) and description."))

class CreateTicketPromptModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(timeout=60.00, *args, **kwargs)
        self.add_item(discord.ui.InputText(label="Ticket Category"))
        self.add_item(discord.ui.InputText(label="Ticket Description", style = discord.InputTextStyle.long))
        
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Modal Results")
        embed.add_field(name="Short Input", value=self.children[0].value)
        embed.add_field(name="Long Input", value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])