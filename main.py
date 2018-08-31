import discord
import discord.ext
from discord.ext import commands
import datetime

import SECRETS
import STATICS


bot = commands.Bot(command_prefix=STATICS.PREFIX, description=" ")
bot_version = "0.1.0"

@bot.event
async def on_ready():
    print("------------Eingeloggt--------------")
    print("Bot Name: " + bot.user.name)
    print("Bot ID: " + bot.user.id)
    print("BOT Version: " + bot_version)
    print("Discord Version: " + discord.__version__)
    print("Datum: " + datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"))
    print("------------------------------------")


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member):
        await bot.kick(member)
        kicker = ctx.message.author
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Kick-Command executed! By:', kicker, '| Kicked:', member)
        await bot.say(embed=discord.Embed(color=discord.Color.dark_red(), description="Applause! Da wurde soeben jemand gekickt!", ))


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member):
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
    await bot.say( embed=discord.Embed(color=discord.Color.dark_orange(), description="*<command> | This are my Commands:"))
    await bot.say("ping | Gives you PONG")
    await bot.say("info | Information about the division")
    await bot.say("kick | Kicks a Member (Use @User)")
    await bot.say("ban | Bans a Member (Use @User)")
    await bot.say("commands | shows my commands")



@bot.command(pass_context=True)
async def info(ctx,):
    # Info Command
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Info-Command executed! By:', executer)
    embed = discord.Embed(title="Division Information",color=discord.Color.dark_green(), description="Infos über die 218.Gaming Division")
    embed.add_field(name="Owner:", value="TheLonelyWolf")
    embed.add_field(name="Gründungsdatum:", value="__***Die 218.Gaming Division wurde am 20. Juni 2018 von TheLonelyWolf gegründet!***__")
    await bot.say(embed=embed)
bot.run(SECRETS.TOKEN)

