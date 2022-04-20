from asyncio import sleep
from sqlite3 import Timestamp
from turtle import title
from xmlrpc.client import DateTime
from music import music_cog
import discord
from youtube_dl import YoutubeDL
import os
from discord.ext import commands
import random
import math
import datetime

bot = commands.Bot(command_prefix = '=', description = 'This is a helper bot')
bot.add_cog(music_cog(bot))

#calculator

def add(n: float, n2: float):
    return n + n2

def sub(n: float, n2: float):
	return n - n2

def rando(n: int, n2: int):
	return random.randint(n, n2)

def div(n: float, n2: float):
	return n / n2

def sqrt(n: float):
	return math.sqrt(n)

def mult(n: float, n2: float):
	return n * n2

@bot.command()
async def dubusum(ctx, x: float, y: float):
	try:
		result = add(x, y)
		await ctx.send(result)

	except:
		pass

@bot.command()
async def dubusub(ctx, x: float, y: float):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass

@bot.command()
async def duburand(ctx, x: int, y: int):
	try:
		result = rando(x, y)
		await ctx.send(result)

	except:
		pass

@bot.command()
async def dubudiv(ctx, x: float, y: float):
	try:
		result = div(x, y)
		await ctx.send(result)

	except:
		pass

@bot.command()
async def dubumult(ctx, x: float, y: float):
	try:
		result = mult(x, y)
		await ctx.send(result)

	except:
		pass

@bot.command()
async def dubusqrt(ctx, x: float):
	try:
		result = sqrt(x)
		await ctx.send(result)

	except:
		pass

#ping
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def twitch(ctx):
    await ctx.send('https://www.twitch.tv/loretokki')

#info
@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="우리 서버 uwu", timestamp= datetime.datetime.utcnow(),color= discord.Color.blue())
    embed.add_field(name="Server created at ", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Master ", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region ", value=f"{ctx.guild.region}")
    await ctx.send(embed=embed)


#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name= "Dubu\'s empress", url="https://www.twitch.tv/loretokki"))
    print('Tamo ready')


bot.run('OTY2NDA2NTExMzYwMzQ0MTM0.YmBSMw.KytfKW3xNp_bnYTH2q3JMwI1_ns')