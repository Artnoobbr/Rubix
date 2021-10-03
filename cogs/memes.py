import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import os

class memes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="incrivel", help="Meme do Senhor Incrivel",aliases=['Incrivel', 'SenhorIncrivel'])
    async def incrivel(self, context, *, text):
        text = text.split('|') #Ele cria uma lista com os conteudos exemplo: ['Bom dia', 'Boa Tarde']
        texto1 = text[0] #Aqui ele vai pegar o item 0 da lista text (usando o exemplo de cima, ele vai pegar o 'Bom dia')
        texto2 = text[1] #Aqui ele vai pegar o item 1 da lista text (usando o exemplo de cima, ele vai pegar o 'Boa Tarde')

        await context.message.delete()

        nome = context.author.name

        img = Image.open('memes/incrivel.jpeg')

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('font/arial.ttf', 30)

        draw.text((25, 26), texto1, (0, 0, 0), font=font)
        draw.text((451, 25), texto2, (0, 0, 0), font=font)

        img.save(f'{nome}.png')

        await context.send(f'{context.author.mention}', file=discord.File(f'{nome}.png'))
        os.remove(f'{nome}.png')

    @commands.command(name='bob', help="Meme do Bob esponja", aliases=['Bob'])
    async def bob(self, context, *, text):
        if text == None:
           await context.reply(f'...Escreva algo para o meme  {context.author.mention} ')
           return
        text = text.split('|')
        texto1 = text[0]
        texto2 = text[1]

        await context.message.delete()

        nome = context.author.name

        img = Image.open('memes/bob.jpg')

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('font/arial.ttf', 35)

        draw.text((395, 51), texto1, (0, 0, 0), font=font)
        draw.text((395, 338), texto2, (0, 0, 0), font=font)

        img.save(f'{nome}.png')

        await context.send(f'{context.author.mention}', file=discord.File(f'{nome}.png'))
        os.remove(f'{nome}.png')

    @commands.command(name='olho', help='Meme Olho', aliases=['Olho', 'olhomeme', 'Olhomeme'])
    async def olho(self, context, *, text=None):
        if text == None:
            await context.reply(f'...Escreva algo para o meme {context.author.mention} ')
            return

        await context.message.delete()

        nome = context.author.name

        img = Image.open('memes/Olho.jpg')
        
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('font/arial.ttf', 45)

        draw.text((76, 497), text, (0, 0, 0), font=font)

        img.save(f'{nome}.png')

        await context.send(f'{context.author.mention}', file=discord.File(f'{nome}.png'))
        os.remove(f'{nome}.png')

    @commands.command(name='cabeca', help='Meme dor de cabeça', aliases=['Cabeca', 'Cabeça', 'cabeça'])
    async def cabeca(self, context, *, text=None):
        if text == None:
            await context.reply(f'...Escreva algo para o meme {context.author.mention} ')
            return

        await context.message.delete()

        nome = context.author.name

        img = Image.open('memes/Cabeça.jpg')
        
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('font/arial.ttf', 35)

        draw.text((265, 315), text, (0, 0, 0), font=font)

        img.save(f'{nome}.png')

        await context.send(f'{context.author.mention}', file=discord.File(f'{nome}.png'))
        os.remove(f'{nome}.png')



def setup(client):
    client.add_cog(memes(client))