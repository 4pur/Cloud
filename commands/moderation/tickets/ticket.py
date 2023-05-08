import discord

from discord.ext import commands
from discord.ui.input_text import InputText

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ticket", aliases=["t"])
    @commands.has_permissions(manage_messages=True)
    async def ticket(self, ctx, title: str = None, desc: str = None, id: int = None):
        e = discord.Embed(title = title, description = desc, color = 0x00ff00)
        e.set_footer(text="Click on the button to make a ticket")
        
        if title == None or desc == None:
            await ctx.send("No title or description, try again.")
        else:
            await ctx.message.delete()
            await ctx.send(embed = e, view = TicketEmbedView(title = title, desc = desc, id = id))

class TicketEmbedView(discord.ui.View):
    def __init__(self, title, desc, id):
        super().__init__()
        self.title = title
        self.desc = desc
        self.id = id

    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.green)
    async def create_ticket(self, x, interaction: discord.Interaction): 
        await interaction.response.send_message("Creating Ticket...", ephemeral=True)
        await interaction.message.delete()
        await interaction.channel.send("Ticket Created!", embed=discord.Embed(title=self.title, description=self.desc))
        await interaction.channel.set_permissions(interaction.user, read_messages=True, send_messages=True)
        await interaction.guild.create_text_channel(name=f"ticket-{interaction.user}", category=self.id, reason=None)
        await interaction.channel.send(f"Ticket Created! <#{interaction.guild.get_channel(interaction.guild.get_channel())}>")
        await interaction.channel.set_permissions(interaction.guild.get_role(interaction.guild.get_channel(interaction.guild.get_channel())), read_messages=False, send_messages=False)