import discord
from discord.ext import commands

TOKEN = 'TOKEN'
prefix = '!'
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents)

initial_extensions = ['commands.commands']

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

@client.event
async def on_ready():
    print(f'{client.user.name} aktif')

client.run(TOKEN)
