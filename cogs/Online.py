import discord
from discord.ext import commands, tasks
from itertools import cycle

class Online(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.status = cycle(['Rubix', 'Versão 1.0', 'sus'])

    @tasks.loop(seconds=60.0)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(self.status)))

    #Evento
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Online "{self.client.user.name}"!')
        self.change_status.start()

def setup(client):
    client.add_cog(Online(client))
