# Used for mass importing commands

from discord.ext import commands
def addCommands(x):
    for command in x:
        commands.add_command(x)