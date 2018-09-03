import threading

import discord
import discord.ext
from discord.ext import commands
import datetime
import asyncio
from boto.s3.connection import S3Connection

import SECRETS
import STATICS


bot = commands.Bot(command_prefix=STATICS.PREFIX, description=" ")
bot_version = "0.1.2"




@bot.event
async def on_ready():
    print("------------Eingeloggt--------------")
    print("Bot Name: " + bot.user.name)
    print("Bot ID: " + bot.user.id)
    print("BOT Version: " + bot_version)
    print("Discord Version: " + discord.__version__)
    print("Datum: " + datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"))
    print("------------------------------------")
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), "RP-Cycle is working!")
        await bot.change_presence(game=discord.Game(name='Wolf.exe | Prefix *'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='Fighting my demons!'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='Playing GOD!'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='Killing Fox.exe!'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='Fox.exe stopped working!'))
        await asyncio.sleep(20)
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), "Restarting RP-Cycle...")


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member):
        await bot.kick(member)
        kicker = ctx.message.author
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Kick-Command executed! By:', kicker, '| Kicked:', member)
        await bot.say(embed=discord.Embed(color=discord.Color.dark_red(), description="Applause! Da wurde soeben jemand gekickt!", ))


@bot.command()
@commands.bot_has_permissions(mention_everyone=True)
async def say(*, content):
    await bot.say(content)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Say-Command executed!')


@bot.command(pass_context=True)
async def wolfbot(ctx):
    executor = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Wolfbot-Command executed! By:', executor)
    emb = discord.Embed(color=discord.Color.dark_orange(), description=bot.user.name)
    emb.add_field(name="Name:", value=bot.user.name)
    emb.add_field(name="Version:", value=bot_version)
    emb.add_field(name="Developer:", value="TheLonelyWolf")
    emb.add_field(name="Mein Zweck:", value="Ich passe auf, dass es keine Anarchy gibt")
    emb.set_footer(text="Discord-Version: " + discord.__version__)
    await bot.say(embed=emb)


@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
@bot.command(pass_context=True)
async def vanish(ctx, number):
    mgs = []  # Empty list to put all the messages in the log
    number = int(number)  # Converting the amount of messages to delete to an integer
    number2 = number + 1
    async for x in bot.logs_from(ctx.message.channel, limit=number2):
        mgs.append(x)
    await bot.delete_messages(mgs)
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Vanish-Command executed! By:', executer)


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
        await bot.ban(member)
        banner = ctx.message.author
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Bann-Command executed! By:', banner, '| Banned:', member)
        await bot.say(embed=discord.Embed(color=discord.Color.dark_red(), description="Applause! Da wurde soeben jemand gebannt!", ))


@bot.command(pass_context=True)
async def ping(ctx,):
    # Ping Command
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Ping-Command executed! By:', executer)
    await bot.say( embed=discord.Embed(color=discord.Color.dark_blue(), description="PONG!"))


@bot.command(pass_context=True)
async def commands(ctx,):
    # Commands Command
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Commands-Command executed! By:', executer)
    emb=discord.Embed(color=discord.Color.dark_orange(), description="Meine Befehle:")
    emb.add_field(name="ping:", value="PONG")
    emb.add_field(name="info:", value="Info über die 218.")
    emb.add_field(name="kick:", value=" Kickt ein User")
    emb.add_field(name="ban:", value="Bannt ein User")
    emb.add_field(name="wolfbot:", value="Info über mich")
    emb.add_field(name="commands:", value="Meine Befehle")
    emb.add_field(name="say:", value="Sende dein Text")
    emb.add_field(name="vanish:", value="Lösche Nachricht(en)")
    emb.set_footer(text="Missbraucht sie ja nicht!")
    await bot.say(embed=emb)


@bot.command(pass_context=True)
async def info(ctx,):
    # Info Command
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Info-Command executed! By:', executer)
    embed = discord.Embed(title="Division Information",color=discord.Color.dark_green(), description="Infos über die 218.Gaming Division")
    embed.add_field(name="Owner:", value="TheLonelyWolf")
    embed.add_field(name="Gründungsdatum:", value="__***Die 218.Gaming Division wurde am 20. Juni 2018 von TheLonelyWolf gegründet!***__")
    await bot.say(embed=embed)

from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['TOKEN'])

bot.run(s3)
