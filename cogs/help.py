import discord
from discord.ext import commands


class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def help(self, context):
        embed = discord.Embed(title=f'Ajuda do {self.client.user.name}',
         color=discord.Color.blue())
        embed.add_field(name='Reddit', value='brasil, meme, smile')
        embed.add_field(name='Memes', value='incrivel(incrivel Texto1 | Texto2), bob(bob Texto | Texto2), olho(olho Texto), cabeca(cabeca Texot)', inline=True)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await context.send(embed=embed)





def setup(client):
    client.add_cog(help(client))