import discord
from dotenv import load_dotenv; load_dotenv() # Read .env file contents
from os import getenv; TOKEN = getenv("TOKEN")

class Cloud(discord.Client):
    async def on_ready(self):
        print(f'online as cloud')

    async def on_message(self, message):
        if message.content == "a":
            print("a")

client = Cloud(intents=discord.Intents.default())
client.run(TOKEN)