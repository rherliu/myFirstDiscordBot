
# coding: utf-8

# In[1]:

#Token: https://discord.com/developers/applications/569131252494368809/bot

import discord
from discord.ext import commands
import networkx as nx

TOKEN='NTY5MTMxMjUyNDk0MzY4ODA5.XLsKyA._3wgRWJcQEkCF9kOi5xNodZKkrA'
bot=commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Bot is already')
    print('-----')

#基礎四則運算：add(+), sub(-), mul(*), div(/)
@bot.command()
async def add(self, a: float, b: float):
    await self.send('和: '+ str(a+b))
    await self.send(a+b)
@bot.command()
async def sub(self, a: float, b: float):
    await self.send('差:')
    await self.send(a-b)
@bot.command()
async def mul(self, a: float, b: float):
    await self.send('積:')
    await self.send(a*b)
@bot.command()
async def div(self, a: float, b: float):
    await self.send('商:')
    await self.send(a/b)

#影片佇列
@bot.command()
async def song(self, x:str):
    video={'1': 'https://www.youtube.com/watch?v=eblocB9LzsA',
           '2': 'https://www.youtube.com/watch?v=vH-sEWbPanU'}
    if x in video:
        await self.send('第' + x + '支影片: ' + video[x])
    elif x == 'all':
        await self.send(video)


bot.run(TOKEN)


# In[1]:

import discord

print(discord.__version__)

