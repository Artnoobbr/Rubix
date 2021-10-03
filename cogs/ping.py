import discord
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commando Pings
    @commands.command(name="ping", help="Mostra a latência do bot",aliases=['Ping'])
    async def ping(self, context):
        await context.message.delete()
        await context.send(f'Pong! ```{round(self.client.latency * 1000)}ms```')


def setup(client):
    client.add_cog(ping(client))
