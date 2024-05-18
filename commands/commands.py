import discord
from discord.ext import commands
import random

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def zarat(self, ctx):
        zar_sonucu = random.randint(1, 6)
        await ctx.send(f'Zar atıldı! Sonuç: {zar_sonucu}')

def setup(client):
    client.add_cog(Commands(client))