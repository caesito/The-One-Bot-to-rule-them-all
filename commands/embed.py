import discord
from discord.ext import commands
from manage_controller.controller import ControllerCharacter
#from mange_api import get


class EmbedCharacter(commands.Cog):
    """ Embend with character """
    def __init__(self, bot):
        self.bot = bot

#race,birth,death,realm,hair, wikiUrl

# Embed
    @commands.command(name= 'info',help= 'informe o nome do personagem ( Iniciais Maiuscula, respeite acentos), Exemplo: Eru Ilúvatar, Gandalf ')
    async def embed_character(self,ctx, *name):
        
        name = ' '.join(name)
        character = ControllerCharacter.controller_character(name)
        print(name)

        name = None
        birth = None
        death = None
        realm = None
        hair = None
        wikiUrl = None

        for item in character:
            name = item['name']
            birth = item['birth']
            death =item['death']
            realm = item['realm']
            hair = item['hair']
            wikiUrl = item['wikiUrl']
            
            
        embed = discord.Embed(
            title = f'{name}',
            description= f'....',
            color = 0x0000FF
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        #embed.set_image(url=url)

        embed.add_field(name='Name:',value= f'{name}')
        embed.add_field(name='Birth: ', value=f'{birth}')
        embed.add_field(name='Death', value= f'{death}')
        embed.add_field(name='Realm', value= f'{realm}')
        embed.add_field(name='Hair', value= f'{hair}')
        embed.add_field(name='Link', value= f'para mais informações sobre {name} acesse: {wikiUrl}')

        await ctx.send(embed= embed)





def setup(bot):
    bot.add_cog(EmbedCharacter(bot))