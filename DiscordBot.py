# coding: utf-8
import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
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
#     await self.send(a+b)
@bot.command()
async def sub(self, a: float, b: float):
    await self.send('差:')
#     await self.send(a-b)
@bot.command()
async def mul(self, a: float, b: float):
    await self.send('積:')
#     await self.send(a*b)
@bot.command()
async def div(self, a: float, b: float):
    await self.send('商:')
#     await self.send(a/b)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

#影片佇列
@bot.command()
async def song(self, x:str):
    video={'1': 'https://www.youtube.com/watch?v=eblocB9LzsA',
           '2': 'https://www.youtube.com/watch?v=vH-sEWbPanU'}
    if x in video:
        await self.send('第' + x + '支影片: ' + video[x])
    elif x == 'all':
        await self.send(video)


# bot.run(TOKEN)
if __name__ == "__main__":
    bot.run(TOKEN)
