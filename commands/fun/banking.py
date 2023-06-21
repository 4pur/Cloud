import os
import random

from   discord.ext import commands

class BankingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Command(name = "deposit", aliases = ["dep"])
    async def deposit(self, ctx, amt):
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
                elif os.path.isfile(f"economy/{ctx.author.id}/bank.txt") is False:
                    with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/last_beg.txt") is False:
                    with open(f"economy/{ctx.author.id}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/last_work.txt") is False:
                    with open(f"economy/{ctx.author.id}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/last_rob.txt") is False:
                    with open(f"economy/{ctx.author.id}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/last_daily.txt") is False:
                    with open(f"economy/{ctx.author.id}/last_daily.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/bank.txt") is False:
                    with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                        x.write("0")
                else:
                    pass
        
        with open(f"economy/{ctx.author.id}/coins.txt", "r") as x:
            coins = int(x.read())
        
        with open(f"economy/{ctx.author.id}/bank.txt", "r") as x:
            bank = int(x.read())
                    
        strings = ['Unfortunately, you are poor, and have no coins to deposit.',
                   'You have deposited no coins into your bank account, sucks to be poor, huh?',
                   'Sadly, you have no coins to deposit.',
                   'You have no coins to deposit, you are such a poor fella.',
                    'I would suggest you to stop playing this game, and get a job.',]
                    
        if amt == None:
            await ctx.send("Please specify an amount to deposit.")
        elif amt == "all":
            if coins == 0:
                await ctx.send(random.choice(strings))
            elif coins == 1:
                await ctx.send(f"You have deposited {coins} coin into your bank account.")   
                
                bank += coins
                coins -= coins
                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coins))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(bank))
            else:
                await ctx.send(f"You have deposited {coins} coins into your bank account.")
                
                bank += coins
                coins -= coins
                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coins))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(bank))
                    
        elif amt == "half":
            if coins == 0:
                await ctx.send(random.choice(strings))
                
            elif coins == 1:
                await ctx.send(f"You have deposited {coins} coin into your bank account.")   
                
                bank += coins
                coins -= coins
                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coins))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(bank))
            else:
                await ctx.send(f"You have deposited {coins / 2} coins into your bank account.")
                
                bank += coins / 2
                coins -= coins / 2
                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coins))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(bank))
                
        elif amt == "quarter":
            await ctx.send(f"You have deposited {coins / 4} coins into your bank account.")
                
            bank += coins / 4
            coins -= coins / 4
            
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                x.write(str(coins))
                
            with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                x.write(str(bank))
                
        else:
            if int(amt) > coins:
                await ctx.send("You do not have enough coins to deposit.")
            else:
                await ctx.send(f"You have deposited {amt} coins into your bank account.")
                
                bank += int(amt)
                coins -= int(amt)
                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coins))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(bank))
                    
    @commands.Command(name = "withdraw", aliases = ["with"])
    async def withdraw(self, ctx, amt):
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
                elif os.path.isfile(f"economy/{ctx.author.id}/bank.txt") is False:
                    with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/last_beg.txt") is False:
                    with open(f"economy/{ctx.author.id}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/last_work.txt") is False:
                    with open(f"economy/{ctx.author.id}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/last_rob.txt") is False:
                    with open(f"economy/{ctx.author.id}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/last_daily.txt") is False:
                    with open(f"economy/{ctx.author.id}/last_daily.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{ctx.author.id}/bank.txt") is False:
                    with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                        x.write("0")
                else:
                    pass
        
        with open(f"economy/{ctx.author.id}/coins.txt", "r") as x:
            coins = int(x.read())
        
        with open(f"economy/{ctx.author.id}/bank.txt", "r") as x:
            bank = int(x.read())
                    
        strings = ['Unfortunately, you are poor, and have no coins to withdraw.',
                   'You have withdrew no coins from your bank account, sucks to be poor, huh?',
                   'Sadly, you have no coins to withdraw.',
                   'You have no coins to withdraw, you are such a poor fella.',
                    'I would suggest you to stop playing this game, and get a job.',]
                    
        if amt == None:
            await ctx.send("Please specify an amount to withdraw.")
        elif amt == "all":
            if coins == 0:
                await ctx.send(random.choice(strings))
            elif coins == 1:
                await ctx.send(f"You have withdrawn {coins} coin from your bank account.")   
                
                coinsa += bank
                banka -= coins

                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coinsa))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(banka))
            else:
                await ctx.send(f"You have withdrawn {coins} coins from your bank account.")
                
                coinsa += bank
                banka -= coins
                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coinsa))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(banka))
                    
        elif amt == "half":
            if coins == 0:
                await ctx.send(random.choice(strings))
                
            elif coins == 1:
                await ctx.send(f"You have withdrawn {coins} coin from your bank account.")   
                
                coinsa += bank
                banka -= coins
                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coinsa))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(banka))
            else:
                await ctx.send(f"You have deposited {coins / 2} coins into your bank account.")
                
                coinsa += bank / 2
                banka -= coins / 2
                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coinsa))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(banka))
                
        elif amt == "quarter":
            await ctx.send(f"You have deposited {coins / 4} coins into your bank account.")
                
            coinsa += banka / 4
            banka -= coins / 4
            
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                x.write(str(coinsa))
                
            with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                x.write(str(banka))
                
        else:
            if int(amt) > coins:
                await ctx.send("You do not have enough coins to deposit.")
            else:
                await ctx.send(f"You have deposited {amt} coins into your bank account.")
                
                coinsa += int(amt)
                banka -= int(amt)
                
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as x:
                    x.write(str(coinsa))
                    
                with open(f"economy/{ctx.author.id}/bank.txt", "w") as x:
                    x.write(str(banka))