import os
from discord.ext import commands

class BankingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def deposit(self, ctx, amt):
        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{ctx.author.id}") == False:
                os.mkdir(f"economy/{ctx.author.id}")
                pass
            else:
                if os.path.isfile(f"economy/{ctx.author.id}/coins.txt") is False:
                    with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                        x.write("0")
                else:
                    pass
        
        with open(f"economy/{ctx.author.id}/coins.txt", "r") as x:
            coins = int(x.read())
                    
        strings = ['Unfortunately, you are poor, and have no coins to deposit.',
                   'You have deposited no coins into your bank account, sucks to be poor, huh?',
                   'Sadly, you have no coins to deposit.',
                   'You have no coins to deposit, you are such a poor fella.',
                    'I would suggest you to stop playing this game, and get a job.',]
                    
        if amt == None:
            await ctx.send("Please specify an amount to deposit.")
        elif amt == "all":
            if coins == 0:
                
                await ctx.send("Unfortunately, you are poor, and have no coins to deposit.")