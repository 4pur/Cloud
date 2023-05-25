import discord
import random
import os

from discord.ext import commands

class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = "balance", aliases = ["bal"])
    async def balance(self, ctx, user: commands.UserConverter = None):
        if user == None:
            identifier = int(ctx.author.id)
                
        if user != None:   
            identifier = user.id

        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass
                    
        with open(f"economy/{identifier}/coins.txt", "r") as f:
            coins = f.read()

        if user is None:
            if int(coins) > 1:
                await ctx.send(f"You have {coins} coins.")
            if int(coins) < 1:
                await ctx.send("You have no coins.")
            if int(coins) == 1:
                await ctx.send(f"You have {coins} coin.")
        else:
            if int(coins) > 1:
                await ctx.send(f"{user.name} has {coins} coins.")
            if int(coins) < 1:
                await ctx.send(f"{user.name} has no coins.")
            if int(coins) == 1:
                await ctx.send(f"{user.name} has {coins} coin.")
        
        
    @commands.command(name = "beg")
    async def beg(self, ctx):
        identifier = int(ctx.author.id)
        
        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass
                    
        with open(f"economy/{identifier}/coins.txt", "r") as f:
            coins = f.read()
        
        with open(f"economy/{identifier}/last_beg.txt", "r+") as f:
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
    @commands.command(name = "pay", aliases = ["give"])
    async def pay(self, ctx, user: commands.UserConverter, amount: int):
        if user is None:
            identifier = int(ctx.author.id)
                
        if user != None:   
            identifier = user.id
            
        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass
        
        with open(f"economy/{ctx.author.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        if int(coins) < amount:
            await ctx.send("You do not have enough coins.")
            return
        
        with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
            f.write(str(int(coins) - amount))
        
        with open(f"economy/{identifier}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        with open(f"economy/{identifier}/coins.txt", "w") as f:
            f.write(str(int(coins) + amount))
        
        await ctx.send(f"You gave {user.mention} {amount} coins.")
        
    @commands.command(name = "coinflip", aliases = ["cf"])
    async def coinflip(self, ctx, amount: int):
        identifier = int(ctx.author.id)
        
        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass
        
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
        identifier = int(ctx.author.id)
        
        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass

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
        if user == None:
            await ctx.send("You didn't specify anyone to rob!")
            return
        if user != None:   
            identifier = user.id

        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass
        
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
            await ctx.send(f"You robbed {user.name} for {rnd2} coins.")

        if rnd < 4:
            await ctx.send(f"You were caught and fined {rnd2} coins.")
            return
        
        if rnd == 4:
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) + rnd2))

            with open(f"economy/{user.id}/coins.txt", "w") as f:
                f.write(str(int(coins) - rnd2))
        elif rnd < 4:
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) + rnd2))

    @commands.command(name = "slots")
    async def slots(self, ctx, amount: int):
        identifier = int(ctx.author.id)
        
        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass
        
        with open(f"economy/{ctx.author.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        if int(coins) < amount:
            await ctx.send("You do not have enough coins.")
            return
        
        rnd1 = random.randint(1, 9)
        rnd2 = random.randint(1, 9)
        rnd3 = random.randint(1, 9)
        
        if rnd1 == rnd2 == rnd3:
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) + amount * 2))
            await ctx.send(f"{rnd1} | {rnd2} | {rnd3}\nYou won {amount * 2} coins.")
        else:
            with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                f.write(str(int(coins) - amount))
            await ctx.send(f"{rnd1} | {rnd2} | {rnd3}\nYou lost {amount} coins.")
            
    @commands.command(name = "daily")
    async def daily(self, ctx):
        identifier = int(ctx.author.id)
        
        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass

        with open(f"economy/{ctx.author.id}/last_daily.txt", "r+") as f:
            last_daily = f.read()
            f.close()
            
        if last_daily != "":
            if int(last_daily) + 86400 > int(ctx.message.created_at.timestamp()):
                await ctx.send("You have to wait a day before claiming your daily coins again.")
                return
        
        with open(f"economy/{ctx.author.id}/last_daily.txt", "w") as f:
            f.write(str(int(ctx.message.created_at.timestamp())))

        with open(f"economy/{ctx.author.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        rnd = random.randint(10, 100)

        with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
            f.write(str(int(coins) + rnd))
        
        await ctx.send(f"You claimed your daily coins. You got {rnd} coins.")
        
    @commands.command(name = "leaderboard")
    async def leaderboard(self, ctx):
        embed = discord.Embed(title = "Leaderboard", description = "Top 10 users with the most coins.", color = 0x00ff00)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/750458012618426133/750458035738474802/coin.png")
        
        for filename in os.listdir("economy"):
            with open(f"economy/{filename}/coins.txt", "r+") as f:
                coins = f.read()
                f.close()
            # Get a users name from their id
            # user = await self.bot.fetch_user(int(filename))
            await embed.add_field(name = f"{self.bot.fetch_user(int(filename)).name}", value = f"{coins} coins", inline = False)
        
        await ctx.send(embed = embed)
        
    @commands.command(name = "shop")
    async def shop(self, ctx):
        embed = discord.Embed(title = "Shop", description = "Buy stuff with your coins.", color = 0x00ff00)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/750458012618426133/750458035738474802/coin.png")
        
        embed.add_field(name = "Laptop", value = "1000 coins", inline = False)
        embed.add_field(name = "PC", value = "5000 coins", inline = False)
        embed.add_field(name = "Phone", value = "10000 coins", inline = False)
        
        await ctx.send(embed = embed)
        
        
    @commands.command(name = "buy")
    async def buy(self, ctx, item: str):
        identifier = int(ctx.author.id)
        
        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass
        
        with open(f"economy/{ctx.author.id}/coins.txt", "r+") as f:
            coins = f.read()
            f.close()
        
        if item == "laptop":
            if int(coins) < 1000:
                await ctx.send("You do not have enough coins.")
                return
            else:
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                    f.write(str(int(coins) - 1000))
                
                with open(f"economy/{ctx.author.id}/laptop.txt", "w") as f:
                    f.write("true")
                    
                await ctx.send("You bought a laptop.")
                
        elif item == "pc":
            if int(coins) < 5000:
                await ctx.send("You do not have enough coins.")
                return
            else:
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                    f.write(str(int(coins) - 5000))
                
                with open(f"economy/{ctx.author.id}/pc.txt", "w") as f:
                    f.write("true")
                    
                await ctx.send("You bought a pc.")
                
        elif item == "phone":
            if int(coins) < 10000:
                await ctx.send("You do not have enough coins.")
                return
            else:
                with open(f"economy/{ctx.author.id}/coins.txt", "w") as f:
                    f.write(str(int(coins) - 10000))
                
                with open(f"economy/{ctx.author.id}/phone.txt", "w") as f:
                    f.write("true")
                    
                await ctx.send("You bought a phone.")
                
        else:
            await ctx.send("That item does not exist.")
            
    @commands.command(name = "inventory")
    async def inventory(self, ctx):
        identifier = int(ctx.author.id)
        
        if os.path.exists("economy") == False:
            os.mkdir("economy")
            pass
        else:
            if os.path.exists(f"economy/{identifier}") == False:
                os.mkdir(f"economy/{identifier}")
                pass
            else:
                if os.path.isfile(f"economy/{identifier}/coins.txt") is False:
                    with open(f"economy/{identifier}/coins.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_beg.txt") is False:
                    with open(f"economy/{identifier}/last_beg.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_work.txt") is False:
                    with open(f"economy/{identifier}/last_work.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_rob.txt") is False:
                    with open(f"economy/{identifier}/last_rob.txt", "w") as x:
                        x.write("0")
                elif os.path.isfile(f"economy/{identifier}/last_daily.txt") is False:
                    with open(f"economy/{identifier}/last_daily.txt", "w") as x:
                        x.write("0")
                else:
                    pass
        
        with open(f"economy/{ctx.author.id}/laptop.txt", "r+") as f:
            laptop = f.read()
            f.close()
        
        with open(f"economy/{ctx.author.id}/pc.txt", "r+") as f:
            pc = f.read()
            f.close()
        
        with open(f"economy/{ctx.author.id}/phone.txt", "r+") as f:
            phone = f.read()
            f.close()
        
        embed = discord.Embed(title = "Inventory", description = "Your inventory.", color = 0x00ff00)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/750458012618426133/750458035738474802/coin.png")
        
        if laptop == "true":
            embed.add_field(name = "Laptop", value = "You own a laptop.", inline = False)
        if pc == "true":
            embed.add_field(name = "PC", value = "You own a PC.", inline = False)
        if phone == "true":
            embed.add_field(name = "Phone", value = "You own a phone.", inline = False)
        
        await ctx.send(embed = embed)