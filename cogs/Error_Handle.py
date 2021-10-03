from datetime import date, datetime
import discord
from discord.ext import commands


class error(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self, context, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
            title='Error Falta de Permissão', 
            description=f'{context.author.mention}, você não tem permissão para executar o comando, verifique se o cargo que você tem tenha as permissões para o comando funcionar',
            color=discord.Color.red(),
            timestamp=datetime.utcnow())
            await context.send(embed=embed)
            await context.message.delete()
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
            title='Error Falta de Algum argumento',
            description=f'{context.author.mention}, você esqueceu algum argumento para o comando funcionar, olhe no ```R>help``` para ver os argumentos necessarios para o comando funcionar',
            color=discord.Color.red(),
            timestamp=datetime.utcnow())
            await context.send(embed=embed)
            await context.message.delete()
        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(
            title='Error Membro não encontrado',
            description=f'{context.author.mention}, O membro que foi usado no comando ou evento não foi encontrado, verifique se o ID ou nick estão corretos',
            color=discord.Color.red(),
            timestamp=datetime.utcnow())
            await context.send(embed=embed)
            await context.message.delete()
        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
            title='Error Comando não foi encontrado',
            description=f'{context.author.mention}, o comando não foi encontrado, verifique se você escreveu o commando corretamente',
            color=discord.Color.red(),
            timestamp=datetime.utcnow())
            await context.send(embed=embed)
            await context.message.delete() 
        elif isinstance(error, commands.CommandOnCooldown):
            await context.send("**Aguarde:** `{:.2f}s` Para executar o comando!".format(error.retry_after))
        elif isinstance(error, commands.BotMissingRole):
            embed = discord.Embed(
            title='Error Bot não tem cargo',
            description=f'"{self.client.user.name}"", não tem o cargo necessario para executar o comando ou evento, verifique se eu possuo o cargo para executar o comando ou evento',
            color=discord.Color.red(),
            timestamp=datetime.utcnow())
            await context.send(embed=embed)
            await context.message.delete()
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
            title='Error falta de Permissão Bot',
            description=f'{self.client.user.name}, não tem permissões para executar o comando ou evento, verifique se o bot tem as permissões para executar o comando ou evento',
            color=discord.Color.red(),
            timestamp=datetime.utcnow())
            await context.send(embed=embed)
            await context.message.delete()
        elif isinstance(error, commands.BotMissingAnyRole): #Ignorar esse por enquanto
            await context.send("Error BotMissingAnyRole")
            await context.message.delete()
        elif isinstance(error, commands.ChannelNotFound):
            embed = discord.Embed(
            title='Error Canal não encontrado',
            description='Não foi possivel encontrar o canal para o evento ou comando',
            color=discord.Color.red(),
            timestamp=datetime.utcnow())
            await context.send(embed=embed)
            await context.message.delete()
        elif isinstance(error, commands.ChannelNotReadable):
            embed = discord.Embed(
            title='Error Canal não legivel',
            description='Não foi possivel ler o canal para o evento ou comando funcionar, verifique as permissões do canal',
            color=discord.Color.red(),
            timestamp=datetime.utcnow())
            await context.send(embed=embed)
            await context.message.delete()

def setup(client):
    client.add_cog(error(client))