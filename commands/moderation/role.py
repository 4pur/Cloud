import discord
from discord.ext import commands

class RoleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="role")
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, role: discord.Role, *, member: discord.Member):
        await member.add_roles(role)
        await ctx.send(f"Added {role.name} to {member.mention}.")
        
    @commands.command(name="removerole", aliases=["rr"])
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, role: discord.Role, *, member: discord.Member):
        await member.remove_roles(role)
        await ctx.send(f"Removed {role.name} from {member.mention}.")