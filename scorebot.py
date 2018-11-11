import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import datetime
import random
import os
from discord import Game
from time import localtime, strftime
strftime("%Y-%m-%d %H:%M:%S", localtime())


Client = discord.client
client = commands.Bot(command_prefix = '^')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game (name="Score Leaderboards", type = 3))
    print("Ready")
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello and welcome to the Prison! Hope you enjoy your stay here!')
    print('Sent message to ' + member.name)

@client.event
async def on_message(message):
    if message.content.startswith('^jokes'):
        randomlist = ["daequan's hairline", "exprisoner's aim", "daily streams by exprisoner"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!time':
        dash = strftime("%I:%M", localtime())
        wholetime = dash[0] + dash[1]
        resttime = dash[2:]
        if int(wholetime) > 12:
            await client.send_message(message.channel, 'The server time now is: **' + wholetime + resttime + 'PM**')
        else:
            await client.send_message(message.channel, 'The server time now is: **' + wholetime + resttime + 'AM**')
client.run('NTEwNzY4NDgyMzE3NTAwNDE4.Dshd7w.IbZyxm3LOPpPvyQRLbr7ffYH9k8')
