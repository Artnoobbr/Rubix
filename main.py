import discord
from discord.ext import commands
import os

from discord.ext.commands.core import command
#import asyncio
#import random
#from datetime import datetime #Embed
#from discord import user #User

#Intents para o discord
intents = discord.Intents.default()
intents.members = True

testing = False

#Client com o prefixo padrão
client = commands.Bot(command_prefix="ru!", intents=intents, help_command=None)

#Comando Clear, vai ficar aqui até eu encontrar um meio de fazer o Purge funcionar
@client.command(name="clear", help="limpa mensagens de uma maneira mais rapida. ```R>Clear <Quantidades de Mensagens> (Não pode passar de 50)```",aliases=['Clear'])
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 10, commands.BucketType.guild)
async def clear(context, number, amount=None):
    if context.author.bot:
        return
    await context.message.delete()
    number = int(number)
    amount = number
    if amount > 50:
        await context.send(f"{context.author.mention}, Não posso apagar mais de 50 mensagens.")
        return
    else:
        await context.channel.purge(limit=amount) and await context.send(f"{amount} Mensagens Apagadas! -{context.author.mention}")
#Processo das Cogs (Não mecher)
extencoes_iniciais = []

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		extencoes_iniciais.append('cogs.' + filename[:-3])

if __name__ == '__main__':
	for extension in extencoes_iniciais:
		client.load_extension(extension)


# Evento para fazer o bot ficar online
client.run('TOKENAQUI')
