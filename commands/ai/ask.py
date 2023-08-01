from os import system

try:
    import openai
except ImportError as e:
    print("openai was not found, installing...")
    system("pip install openai")
    
    import openai

import discord
import os

from   discord.ext import commands
from   dotenv      import load_dotenv
from   openai      import ChatCompletion

load_dotenv()
openai.api_key = os.getenv("OPENAI_TOKEN")

class AskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ai", aliases=["askai", "openai", "gpt", "ask", "g"])
    async def ask(self, ctx, *, x = None):
        response = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chat bot inside of a Discord server. Your name is Cloud. You respond to queries users ask you, which could be anything. Your goal is to be pleasant and welcoming. User input may be multi-line, and you can respond with multiple lines as well. Here are some examples:"},
                {"role": "system", "content": "Your responses are to be human-like."},
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
            async with ctx.typing():
                await ctx.send(response)