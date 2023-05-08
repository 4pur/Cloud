import discord

from discord.ext import commands
from discord.ui.input_text import InputText

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ticket", aliases=["t"])
    @commands.has_permissions(manage_messages=True)
    async def ticket(self, ctx, title, desc):
        await ctx.send("creating embed...", view=TicketEmbedView(title = title, desc = desc))
        

class TicketEmbedView():
    def __init__(self, title, desc, *args, **kwargs):
        super.__init__(title, desc, *args, **kwargs)
        this.title = title
        this.desc = desc
        e = discord.Embed(title=title, description=desc)
        e.set_footer(text="")