import discord
from discord import message
from discord.ext import commands
from datetime import datetime


class admins(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #Comando de Ban
    @commands.command(name="ban", help="Bane alguém do seu servidor. ```R>ban <ID ou marque a pessoa> (Motivo)```",aliases=['Ban'])
    @commands.cooldown(2, 5, commands.BucketType.guild)
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member, *, reason = None):
        if context.author.bot:
            await context.message.delete()
            return
        elif member == context.author:
            await context.message.delete()
            await context.send('Você não pode se banir Bobinho!')
            return
        elif member == discord.NotFound:
            await context.message.delete()
            await context.send(f'O {member}, não foi encontrado')
            return
        #Embeds
        embed_ban = discord.Embed(
        title=f'O {member} foi banido!', 
        description=f'Motivo: {reason}', 
        color=discord.Color.green(), 
        timestamp= datetime.utcnow())
        embed_ban.set_footer(text=f'ID: {member.id}, Autor do Banimento: {context.author}')

        embed_error = discord.Embed(
        title=f'Algo deu errado!', 
        description=f'Verfique se o bot está com cargo maior que {member.mention}, para poder banir',
        color=discord.Color.red(), 
        timestamp=datetime.utcnow())
        embed_error.set_footer(text=f'ID: {member.id}')

        #Processo Do banimento
        try:
            await member.ban(reason=reason)
            await context.message.delete()
            await context.send(embed=embed_ban)
            
        except:
            await context.message.delete()
            await context.send(embed=embed_error)
            return
    
    @commands.command(name="unban", help="desbane alguém do seu servidor. ```R>unban <ID da pessoa> (Motivo)```", aliases=['Unban'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, context, user: discord.User, *, reason=None):
        if context.author.bot:
            await context.message.delete()
            return
        elif user == context.author:
            await context.send(
            f'Você não pode se desbanir {context.author.mention}... *Até porque você não está banido em primeiro lugar!*')
            return

        guild = context.guild
        #Embeds
        embed_unban = discord.Embed(
        title=f'O {user} foi desbanido!', 
        description=f'Motivo: {reason}', 
        color=discord.Color.green(), 
        timestamp=datetime.utcnow())
        embed_unban.set_footer(text=f'ID: {user.id}')

        embed_error = discord.Embed(
        title=f'Algo deu errado!', 
        description=f'Verfique se: O "{user}" está na lista de banimentos',
        color=discord.Color.red(), 
        timestamp=datetime.utcnow())
        embed_error.set_footer(text=f'ID: {user.id}')

        #Processo do Unban
        try:
            await guild.unban(user=user, reason=reason)
            await context.message.delete()
            await context.send(embed=embed_unban)
        except:
            await context.message.delete()
            await context.send(embed=embed_error)




def setup(client):
    client.add_cog(admins(client))