import random
import os

from discord.ext import commands

class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = "balance", aliases = ["bal"])
    async def balance(self, ctx, user: commands.UserConverter = None):
        if user == None:
            print(ctx.author.id)
            await self.makeFiles(identifier = ctx.author.id)
            with open(f"economy/{ctx.author.id}/coins.txt", "r") as f:
                coins = f.read()
        else:
            print(user.id)
            await self.makeFiles(identifier = user.id)
            with open(f"economy/{user.id}/coins.txt", "r") as f:
                coins = f.read()

        if user == None:
            if int(coins) > 1:
                await ctx.send(f"You have {coins} coins.")
            if int(coins) == 1:
                await ctx.send(f"You have {coins} coin.")
        else:
            if int(coins) > 1:
                await ctx.send(f"{user.id} has {coins} coins.")
            if int(coins) == 1:
                await ctx.send(f"{user.id} has {coins} coin.")
        
        
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
        
        with open(f"economy/{user}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        with open(f"economy/{user}/coins.txt", "w") as f:
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

    @commands.command(name = "work")
    async def work(self, ctx):
        await self.make_account(ctx = ctx, user = None)

        with open(f"economy/{ctx.author.id}/last_work.txt", "r+") as f:
            last_work = f.read()
            f.close()
            
        if last_work != "":
            if int(last_work) + 14400 > int(ctx.message.created_at.timestamp()):
                await ctx.send("You have to wait four hours before working again.")
                return
        
        with open(f"economy/{ctx.author.id}/last_work.txt", "w") as f:
            f.write(str(int(ctx.message.created_at.timestamp())))

        with open(f"economy/{ctx.author.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        rnd = random.randint(10, 300)

        if rnd < 30:
            await ctx.send("You were mugged on the way home for 30 coins")
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) - 30))

        
        if rnd > 270:
            await ctx.send("You were robbed on the way home for 200 coins")
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) - 200))
            return
        
        with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
            f.write(str(int(coins) + rnd))
        
        await ctx.send(f"You worked for {rnd} coins.")

    @commands.command(name = "rob")
    async def rob(self, ctx = None, user: commands.UserConverter = None):
        await self.make_account(ctx = ctx, user = user)
        
        with open(f"economy/{ctx.author.id}/last_rob.txt", "r+") as f:
            last_rob = f.read()
            f.close()
            
        if last_rob != "":
            if int(last_rob) + 1800 > int(ctx.message.created_at.timestamp()):
                await ctx.send("You have to wait 30 minutes before robbing someone again.")
                return
        
        with open(f"economy/{ctx.author.id}/last_rob.txt", "w") as f:
            f.write(str(int(ctx.message.created_at.timestamp())))

        with open(f"economy/{ctx.author.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        rnd = random.randint(1, 4)
        rnd2 = random.randint(20, 100)

        if rnd == 4:
            await ctx.send(f"You robbed {user} for {rnd2} coins.")

        if rnd < 4:
            await ctx.send(f"You were caught and fined {rnd2} coins.")
            return
        
        if rnd == 4:
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) + rnd2))

            with open(f"economy/{user}/coins.txt", "w") as f:
                f.write(str(int(coins) - rnd2))
        elif rnd < 4:
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) + rnd2))
    async def make_account(self, ctx, user: commands.UserConverter):
        if ctx == None: 
            userId = user.id
        else: 
            userId = ctx.author.id
        await self.makeFiles(userId)

    async def makeFiles(identifier):
        files = ["coins", "last_beg", "last_work", "last_rob"]
       

            
        if os.path.exists("economy") == False:
            os.mkdir("economy")
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
            else:
                for str in files:
                    if os.path.isfile(f"economy/{identifier}/{str}.txt") == False:
                        with open(f"economy/{identifier}/{str}.txt", "w") as x:
                            x.write("0")
                    else:
                        print("")