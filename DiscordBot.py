# coding: utf-8
import os
# import discord
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
    await self.send('sum: '+ str(a+b))

@bot.command()
async def sub(self, a: float, b: float):
    await self.send('difference:')

@bot.command()
async def mul(self, a: float, b: float):
    await self.send('product:')

@bot.command()
async def div(self, a: float, b: float):
    await self.send('quotient:')

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)
