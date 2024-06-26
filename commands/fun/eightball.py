import random

from discord.ext import commands

class EightballCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="8ball", aliases=["eightball", "8b"])
    async def eightball(self, ctx, a, *, question):
        if a == "ask":
            responses = ["It is certain.",
                        "It is decidedly so.",
                        "Without a doubt.",
                        "Yes - definitely.",
                        "You may rely on it.",
                        "As I see it, yes.",
                        "Most likely.",
                        "Outlook good.",
                        "Yes.",
                        "Signs point to yes.",
                        "Reply hazy, try again.",
                        "Ask again later.",
                        "Better not tell you now.",
                        "Cannot predict now.",
                        "Concentrate and ask again.",
                        "Don't count on it.",
                        "My reply is no.",
                        "My sources say no.",
                        "Outlook not so good.",
                        "Very doubtful."]
            
        elif a == "yes_or_no":
            responses = ["Yes.",
                         "No."]
            
        else:
            ctx.send("Invalid argument. Valid arguments are `ask` and `yes_or_no`.")
        
        await ctx.send(f"{random.choice(responses)}")