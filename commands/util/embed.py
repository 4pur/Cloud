import discord

from discord.ext import commands
from discord.ui.input_text import InputText

class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="embed")
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx):
        await ctx.send(view = EmbedView())

class EmbedModalCreator(discord.ui.Modal):
    def __init__(self, custom_id):
        super().__init__(title = "Embed Creator")
        self.custom_id = custom_id
        
        self.add_item(InputText(label="Title", placeholder="Enter a title", custom_id="title"))
        self.add_item(InputText(label="Description", placeholder="Enter a description", custom_id="desc")) 
        
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title = self.children[0].value)
        embed.add_field(name = "", value=self.children[1].value)
        
        await interaction.channel.send(embed=embed)

class EmbedView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Create Form", style=discord.ButtonStyle.green, custom_id="create_embed_form")
    
    async def callback(self, x, interaction: discord.Interaction):
        await interaction.response.send_modal(EmbedModalCreator(custom_id = "embed_form"))