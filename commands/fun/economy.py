import random
import os

from discord.ext import commands

class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = "balance", aliases = ["bal"])
    async def balance(self, ctx, user: commands.UserConverter = None):
        if user == None:
            a = ctx.author
        else:
            a = user
            
        await self.make_account(user = a)
        
        with open(f"economy/{a.id}/coins.txt", "r") as f:
            coins = f.read()
        
        if user == None:
            if int(coins) > 1:
                await ctx.send(f"You have {coins} coins.")
            if int(coins) == 1:
                await ctx.send(f"You have {coins} coin.")
        else:
            if int(coins) > 1:
                await ctx.send(f"{user.name} has {coins} coins.")
            if int(coins) == 1:
                await ctx.send(f"{user.name} has {coins} coin.")
        
        
    @commands.command(name = "beg")
    async def beg(self, ctx):
        await self.make_account(ctx)
        
        with open(f"economy/{ctx.author.id}/last_beg.txt", "r+") as f:
            last_beg = f.read()
            f.close()
            
        if last_beg != "":
            if int(last_beg) + 3600 > int(ctx.message.created_at.timestamp()):
                await ctx.send("You have to wait an hour before begging again.")
                return
        
        with open(f"economy/{ctx.author.id}/last_beg.txt", "w") as f:
            f.write(str(int(ctx.message.created_at.timestamp())))
        
        with open(f"economy/{ctx.author.id}/coins.txt", "r") as f:
            coins = f.read()
            f.close()
        
        if int(coins) < 0:
            await ctx.send("You have no coins.")
            return
        
        rnd = random.randint(1, 100)
        
        if rnd < 10:
            await ctx.send("You were caught begging and were fined 10 coins.")
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) - 10))
            return
        
        if rnd > 90:
            await ctx.send("You were caught begging and were fined 5 coins.")
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) - 5))
            return
        
        with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
            f.write(str(int(coins) + rnd))
        
        await ctx.send(f"You begged and got {rnd} coins.")
        
    
        with open(f"economy/{ctx.author.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
    @commands.command(name = "pay")
    async def pay(self, ctx, user: commands.UserConverter, amount: int):
        await self.make_account(ctx = ctx, user = user)
        
        with open(f"economy/{ctx.author.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        if int(coins) < amount:
            await ctx.send("You do not have enough coins.")
            return
        
        with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
            f.write(str(int(coins) - amount))
        
        with open(f"economy/{user.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        with open(f"economy/{user.id}/coins.txt", "w") as f:
            f.write(str(int(coins) + amount))
        
        await ctx.send(f"You gave {user.mention} {amount} coins.")
        
    @commands.command(name = "coinflip", aliases = ["cf"])
    async def coinflip(self, ctx, amount: int):
        await self.make_account(ctx)
        
        with open(f"economy/{ctx.author.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        if int(coins) < amount:
            await ctx.send("You do not have enough coins.")
            return
        
        rnd = random.randint(1, 2)
        
        if rnd == 1:
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) - amount))
            await ctx.send(f"You lost {amount} coins.")
        else:
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) + amount))
            await ctx.send(f"You won {amount} coins.")
        
    async def make_account(self, ctx = None, user: commands.UserConverter = None):
        if ctx == None:
            pass
        else:
            if os.path.exists(f"economy/{ctx.author.id}") == False:
                os.mkdir(f"economy/{ctx.author.id}")
                
            if os.path.exists(f"economy/{ctx.author.id}/coins.txt") == False:
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                    f.write("0")
                    
            if os.path.exists(f"economy/{ctx.author.id}/last_beg.txt") == False:
                with open(f"economy/{ctx.author.id}/last_beg.txt", "w") as f:
                    f.write("0")
                    
        if user == None:
            pass
        else:
            if os.path.exists(f"economy/{user.id}") == False:
                os.mkdir(f"economy/{user.id}")
                
            if os.path.exists(f"economy/{user.id}/coins.txt") == False:
                with open(f"economy/{user.id}/coins.txt", "w") as f:
                    f.write("0")
                    
            if os.path.exists(f"economy/{user.id}/last_beg.txt") == False:
                with open(f"economy/{user.id}/last_beg.txt", "w") as f:
                    f.write("0")