import discord
from discord.ext import commands

class AutoroleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="autorole")
    @commands.has_permissions(manage_roles=True)
    async def autorole(self, ctx, role: discord.Role):
        with open(f'roles/{ctx.guild.id}.csv', 'a') as w:
            w.write(str(role.id))
        await ctx.send(f"Set autorole to {role.mention}.")
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open(f'roles/{member.guild.id}.csv', 'r') as r:
            await member.add_roles(discord.utils.get(member.guild.roles, id=int(r.read())))