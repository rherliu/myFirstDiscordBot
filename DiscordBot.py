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
    await self.send('sum: '+str(a+b))

@bot.command()
async def sub(self, a: float, b: float):
    await self.send('difference:'+str(a-b))

@bot.command()
async def mul(self, a: float, b: float):
    await self.send('product:'+str(a*b))

@bot.command()
async def div(self, a: float, b: float):
    await self.send('quotient:'+str(a/b))

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    
@bot.command()
async def BinaryEquation(self, a:str, b:str, c:str):
    A = a.split("/")
    B = b.split("/")
    C = c.split("/")
    outputA = int(A[0]) / int(A[1])
    outputB = int(B[0]) / int(B[1])
    outputC = int(C[0]) / int(C[1])
    d = (outputB * outputB - 4 * outputA * outputC)**0.5
    await self.send("x1="+str(((-1 * outputB) + d) / (2 * outputA)))
    await self.send("x2="+str(((-1 * outputB) - d) / (2 * outputA)))

@bot.command()
async def clean(ctx, num:int):
    await ctx.channel.purge(limit = num+1)

if __name__ == "__main__":
    bot.run(TOKEN)
