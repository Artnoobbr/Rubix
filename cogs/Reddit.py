import discord
from discord import message
from discord.ext import commands
from datetime import datetime
import random
import asyncpraw

reddit = asyncpraw.Reddit(
    client_id="iuKD-jsuCm_DipYsy__-GQ",
    client_secret="DTjHFhgzvy8UNDRJvbAHotIENkaReg",
    user_agent="Rubix",
)


class reddit_command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='brasil')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def brasil(self, context):
        await context.message.delete()
        msg = await context.send('Carregando meme...')
        subreddit = await reddit.subreddit("MemesBrasil")
        lista_subs = []
        top = subreddit.top(limit = 250)
        async for submission in top:
            lista_subs.append(submission)
    
        submission_aleatoria = random.choice(lista_subs)

        nome = submission_aleatoria.title
        link = submission_aleatoria.url
        author = submission_aleatoria.author

        embed = discord.Embed(title=f'{nome}', color=discord.Color.random(), timestamp=datetime.utcnow(), url=link)
        embed.set_image(url=link)
        embed.set_footer(text=f"Distribuido pelo r/MemesBrasil! | Autor do Post: {author}")
        await context.send(embed=embed)
        await msg.edit(content='Aqui está! :white_check_mark:')

    @commands.command(name='meme')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def meme(self, context):
        await context.message.delete()
        msg = await context.send('Carregando meme...')
        subreddit = await reddit.subreddit("Memes")
        lista_subs = []
        top = subreddit.top(limit = 350)
        async for submission in top:
            lista_subs.append(submission)
    
        submission_aleatoria = random.choice(lista_subs)

        nome = submission_aleatoria.title
        link = submission_aleatoria.url
        author = submission_aleatoria.author

        embed = discord.Embed(title=f'{nome}', color=discord.Color.random(), timestamp=datetime.utcnow(), url=link)
        embed.set_image(url=link)
        embed.set_footer(text=f"Distribuido pelo r/Memes! | Autor do Post: {author}")
        await context.send(embed=embed)
        await msg.edit(content='Aqui está! :white_check_mark:')

    @commands.command(name='smile')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def smile(self, context):
        await context.message.delete()
        msg = await context.send('Pegando alguma postagem...')
        subreddit = await reddit.subreddit("MadeMeSmile")
        lista_subs = []
        top = subreddit.top(limit = 200)
        async for submission in top:
            lista_subs.append(submission)
    
        submission_aleatoria = random.choice(lista_subs)

        nome = submission_aleatoria.title
        link = submission_aleatoria.url
        author = submission_aleatoria.author

        embed = discord.Embed(title=f'{nome}',color=discord.Color.random(), timestamp=datetime.utcnow(), url=link)
        embed.set_image(url=link)
        embed.set_footer(text=f"Distribuido pelo r/MadeMeSmile! | Autor do Post: {author}")
        await context.send(embed=embed)
        await msg.edit(content='Aqui está! :white_check_mark:')





def setup(client):
    client.add_cog(reddit_command(client))
