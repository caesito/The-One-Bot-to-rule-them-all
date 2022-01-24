#pip install discord.py
#PIP INSTALL PYTHON-DECOUPLE
import discord
from decouple import config
from discord.ext import commands,tasks
import os


bot = commands.Bot("!")

def load_cogs(bot):

    bot.load_extension('manager')
    bot.load_extension('commands.embed')
    
    
load_cogs(bot)

TOKEN = config('TOKEN')
bot.run(TOKEN)


