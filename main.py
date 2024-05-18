import discord
from discord.ext import commands

TOKEN = 'TOKEN'
prefix = '!'
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} aktif')


client.run(TOKEN)
