import discord
import openai
import os


from discord.ext import commands
from dotenv import load_dotenv
from openai import ChatCompletion

load_dotenv()
api_key = os.getenv("OPENAI_TOKEN")

class AskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ask", aliases=["askai", "openai", "gpt"])
    async def ask(self, ctx, prompt: discord.Message = None):
        response = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ]
        )
        
        response_text = response['choices'][0]['message']['content']
        
        responses = []
        if len(response_text) > 2000:
            responses = [
                response_text[i : i + 2000] for i in range(0, len(response_text), 2000)
            ]
        else:
            responses.append(response_text)
            
        for response in responses:
            await ctx.send(response)