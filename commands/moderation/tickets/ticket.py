import discord

from discord.ext import commands
from discord.ui.input_text import InputText

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ticket", aliases=["t"])
    @commands.has_permissions(manage_messages=True)
    async def ticket(self, ctx, title: str = None, desc: str = None):
        await ctx.send(view = TicketEmbedView(), delete_after = 60)
        


class TicketEmbedModalCreator(discord.ui.Modal):
    def __init__(self, custom_id):
        super().__init__(title = "Ticket Creator")
        self.custom_id = custom_id
        
        self.add_item(InputText(label="Title", placeholder="Enter a title", custom_id="title"))
        self.add_item(InputText(label="Description", placeholder="Enter a description", custom_id="desc"))
        self.add_item(InputText(label="Category ID", placeholder="Enter a category ID for tickets to be created in", custom_id="id"))
        
        
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(self.children[0].value)
        embed.add_field(value=self.children[1].value)
        global category
        catergory = self.children[2].value
        interaction.channel.send(embed=embed)

class TicketEmbedView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Create Form", style=discord.ButtonStyle.green, custom_id="create_ticket_form")
    
    async def callback(self, x, interaction: discord.Interaction):
        await interaction.response.send_modal(TicketEmbedModalCreator(custom_id="ticket"))