import discord

from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from openai import ChatCompletion, api_key



class AskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ask(ctx, message: discord.Message):
        load_dotenv()
        api_key = getenv("OPENAI_API_KEY")

        response = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": text},
            ]
        )

        rt = response['choices'][0]['message']['content']
        
        responses = []
        if len(rt) > 2000:
            responses = [
                rt[i : i + 2000] for i in range(0, len(rt), 2000)
            ]
        else: # if not too long just append the full rt
            responses.append(rt)

        try:
            for response in responses:
                await message.channel.send(response)
        except:
            await message.channel.send("Something went wrong. Please try again later.")