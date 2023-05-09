import discord

from discord.ext import commands
from discord.ui.input_text import InputText

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ticket", aliases=["t"])
    @commands.has_permissions(manage_messages=True)
    async def ticket(self, ctx, title: str = None, desc: str = None, id: discord.CategoryChannel = None):
        e = discord.Embed(title = title, description = desc, color = 0x00ff00)
        e.set_footer(text="Click on the button to make a ticket")
        
        if title == None or desc == None:
            await ctx.send("No title or description, try again.")
        else:
            await ctx.message.delete()
            await ctx.send(embed = e, view = TicketEmbedView())


class TicketEmbedModalCreator(discord.ui.Modal):
    def __init__(self, custom_id):
        super().__init__(timeout=None)
        self.custom_id = custom_id
        
        self.add_item(InputText(label="Title", placeholder="Enter a title", custom_id="title"))
        self.add_item(InputText(label="Description", placeholder="Enter a description", custom_id="desc"))
        self.add_item(InputText(label="Category ID", placeholder="Enter a category ID for tickets to be created in", custom_id="id"))

class TicketEmbedView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(TicketEmbedModalCreator(custom_id="ticket"))