import discord
from dotenv import load_dotenv; load_dotenv() # Read .env file contents
from os import getenv; TOKEN = getenv("TOKEN")

class Cloud(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = Cloud()
client.run(TOKEN)