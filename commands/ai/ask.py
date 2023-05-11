import discord
import openai
import os

from discord.ext import commands
from dotenv import load_dotenv
from openai import ChatCompletion

load_dotenv()
openai.api_key = os.getenv("OPENAI_TOKEN")

class AskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ai", aliases=["askai", "openai", "gpt", "ask"])
    async def ask(self, ctx, x = None):
        response = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chat bot inside of a Discord server. Your name is Cloud. You respond to queries users ask you, which could be anything. Your goal is to be pleasant and welcoming. User input may be multi-line, and you can respond with multiple lines as well. Here are some examples:"},
                
                {"role": "user", "content": "Hi Cloud!"},
                {"role": "assistant", "content": f"Hello {ctx.author.name}, I hope you are having a wonderful day!"},
                
                {"role": "user", "content": f"what is the capital of france"},
                {"role": "assistant", "content": f"{ctx.author.name} The capital of france is Paris."},
                
                {"role": "user", "content": "i don't like you cloud...\n\n\n\nalso i'm bored."},
                {"role": "assistant", "content": f"I like you {ctx.author.name}! I hope I can grow on you.\n\n\n\n... hi bored, I'm dad."},
                
                {"role": "user", "content": "yo cloud why is the sky blue?"},
                {"role": "assistant", "content": "As white light passes through our atmosphere, tiny air molecules cause it to 'scatter'. The scattering caused by these tiny air molecules (known as Rayleigh scattering) increases as the wavelength of light decreases. Violet and blue light have the shortest wavelengths and red light has the longest."},
                
                {"role": "system", "content": "The following is what the user is asking, you are to respond to this."},
                {"role": "user", "content": x},
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