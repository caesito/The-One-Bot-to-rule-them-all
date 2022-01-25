import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument


class Manager(commands.Cog):
    """ Maneger bot """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'estou logado como {self.bot.user}')
        
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('coloque todos argumentos, digite !help para ver os comandos')
        elif isinstance(error, CommandNotFound):
            await ctx.send(' comando nao existe, digite !help para ver os comandos')
        else:
            raise error
          
def setup(bot):
    bot.add_cog(Manager(bot))