import aiohttp
import os
import discord
import discord.ext
from discord.ext import commands
import datetime
import asyncio
import random
from random import randint
import time
import sys
import json

import Config

bot = commands.Bot(command_prefix=Config.PREFIX, description=" ")
bot_version = Config.Version

epoch = datetime.datetime.utcfromtimestamp(0)

players = {}


# ------------------------------
# Responses
# ------------------------------
# ------------------------------


killResponses = ("%s ist aus Versehen in die Lave geschupst worden. UPS",
                 "%s ist auf ein Wolf gestoßen, danach hörte man nichts mehr von ihm.",
                 "Ich habe %s mal um die Ecke gebracht, kam alleine zurück.",
                 "Hat wer %s gesehen? War vorher mit ihm am Fluss.",
                 "Ich habe %s vergiftet. Wer möchte einen sterbenden %s sehen?",
                 "Habe %s 's Kopf weggerissen und in Mülleimer geworfen.",
                 "%s findet sein Gehirn nichtmehr. *Psst! Ich habs zerschrettert, sag es aber niemanden*",
                 "Sorry %s, aber ich musste dich leider erschießen.")

yodaResponses = ("Schlafen du jetzt musst, sonst du morgen müde sein wirst.",
                 "Unmöglich zu sehen, die Zukunft ist.",
                 "Groß machen Kriege niemand.",
                 "Furcht der Pfad zur dunklen Seite ist.",
                 "Eure Sinne ihr nutzen müsst.",
                 "Die Macht stark in dir ist.",
                 "Grammatik ich von Yoda gelernt haben.",
                 "Viel zu lernen du noch hast, mein junger Padawan.",
                 "Tue es oder tue es nicht! Versuchen es nicht gibt.",
                 "Die macht nur zur Verteidigung benutzen du darfst. Niemals zum Angriff!",
                 "Dich lebend zu sehen mich erfreut, %s",
                 "Der Tod ein natürlicher Bestandteil des Lebens ist.",
                 "Ins Exil ich muss, versagt ich haben.",
                 "Feigling du bist, wenn du folgen der dunklen Seite.",
                 "Kleine Truppe wir sind, dafür größer im Geist.",
                 "Deine Wahrnehmung deine Realität bestimmen wird.",
                 "Geburtstag du hast! Alter Sack du jetzt bist.",
                 "Müde ich bin, Kaffee ich jetzt brauch.",
                 "Montag! Schrecklich er ist.",
                 "Schnauze halten du musst, bis ich Kaffee fertig getrunken habe.",
                 "Möge das Wetter mit deuch sein.",
                 "Yodafone - Der Internetanbieter für Jedis",
                 "Kaffee du bringen mir musst, sonst töten ich dich werde.",
                 "Die dunkle Seite stärker als Chuck Norris ist.",
                 "Auf dein Herz hören du musst, um zu erfüllen deine Träume.",
                 "Du nicht grundlos töten darfst!")


# ------------------------------
# On_Ready Output
# ------------------------------
# ------------------------------


@bot.event
async def on_ready():
    print("------------Eingeloggt--------------")
    print("Bot Name: " + bot.user.name)
    print("Bot ID: " + bot.user.id)
    print("Bot Version: " + bot_version)
    print("Discord Version: " + discord.__version__)
    print("Datum: " + datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"))
    servers = list(bot.servers)
    print("Connected on '" + str(len(bot.servers)) + "' servers!")
    print("------------------------------------")
    bot.loop.create_task(status_task())
    print("Running on: " + sys.platform)


# ------------------------------
# On_Message Output
# ------------------------------
# ------------------------------


@bot.event
async def on_message(message):
    user = message.author
    channel = message.channel
    msg = message.content
    server = message.author.server
    if message.author == bot.user:
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S] S:{}|C:{}| Bot antwortete:".format(server,channel)), msg)
    else:
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S] S:{}|C:{}|".format(server,channel)), user, ":", msg)
        await bot.process_commands(message)


# ------------------------------
# Playing Status
# ------------------------------
# ------------------------------


async def status_task():
    await asyncio.sleep(2)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), "RP-Cycle is starting!")
    while True:
        servers = list(bot.servers)
        await bot.change_presence(game=discord.Game(name=("Running on: [" + str(len(bot.servers)) + "] Server!")))
        await asyncio.sleep(2)


# ------------------------------
# Choose Command
# ------------------------------
# ------------------------------


@bot.command()
async def discordversion():
    await bot.say("Discord Version: " + discord.__version__)


# ------------------------------
# Choose Command
# ------------------------------
# ------------------------------


@bot.command()
async def choose(*choices : str):
    Choosing = random.choice(choices)
    embed = discord.Embed(color=discord.Color.dark_grey())
    embed.add_field(name="Ich habe folgendes gewählt:", value=Choosing)
    embed.add_field(name="Zur Auswahl standen:", value=choices, inline=False)
    await bot.say(embed=embed)

# ------------------------------
# Bitcoin Command
# ------------------------------
# ------------------------------


@bot.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await bot.say("Derzeitiger Wert des Bitcoins: $" + response['bpi']['USD']['rate'])
# ------------------------------
# Profile Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def profile(ctx, member: discord.Member = None):
    if member == None:
        author = ctx.message.author
        avatar = ctx.message.author.avatar_url
        joined = author.joined_at.__format__('%A, %d. %B %Y um %H:%M:%S')
        toprole = ctx.message.author.top_role
        nicker = ctx.message.author.nick
        userID = ctx.message.author.id
    else:
        author = member.name
        avatar = member.avatar_url
        joined = member.joined_at.__format__('%A, %d. %B %Y um %H:%M:%S')
        toprole = member.top_role
        nicker = member.nick
        userID = member.id
    embed = discord.Embed(title="User Information", color=discord.Color.dark_grey(),)
    embed.add_field(name="Username:", value=author)
    embed.set_thumbnail(url=avatar)
    embed.add_field(name='Nickname:', value=nicker, inline=True)
    embed.add_field(name='User ID:', value=userID, inline=False)
    embed.add_field(name="Höchste Role:", value=toprole, inline=False)
    embed.add_field(name='Beigetreten am:', value=joined, inline=False)
    executor = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Profile-Command executed! By:', executor)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Profile shown from:', author)
    await bot.say(embed=embed)


# ------------------------------
# Kill Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def kill(ctx, *, member: discord.Member = None):
    executor = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Kill-Command executed! By:', executor)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Versuchte Mord von: ', member)
    if member is None:
        await bot.say("Wenn ich das Universum töte bleibt nichts mehr übrig und das möchte ich nicht!")
        return

    if member.id == "484382176180305950":
        await bot.say("Mich kann man nicht töten! Ich bin der Tod! :knife: ")
    elif member.id == "484382176180305950" and ctx.message.author.id == "261179915892686849":
        await bot.say("Ich möchte dich aber nicht töten, Meister!")
    elif member.id == "261179915892686849":
        await bot.say("Ich töte meinen Meister nicht!")
    elif member.id == ctx.message.author.id:
        await bot.say("Du kannst auch Selbstmord betreiben. Dann mach ich mir die Hände nicht schmutzig!")
    else:
        choice = killResponses[random.randrange(0, len(killResponses))] % member.mention
        await bot.say(choice)


# ------------------------------
# Yoda Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def yoda(ctx, *, member: discord.Member = None):
    executor = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Yoda-Command executed! By:', executor)
    choice = yodaResponses[random.randrange(0, len(yodaResponses))]
    await bot.say(embed=discord.Embed(color=discord.Color.dark_green(), description=choice))


# ------------------------------
# Say Command
# ------------------------------
# ------------------------------


@bot.command()
@commands.bot_has_permissions(mention_everyone=True)
async def say(*, content):
    await bot.say(content)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Say-Command executed!')


# ------------------------------
# Wolfbot Command
# ------------------------------
# ------------------------------


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


# ------------------------------
# Vanish Command
# ------------------------------
# ------------------------------


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


# ------------------------------
# Kick Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None):
    kicker = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Kick-Command executed! By:', kicker, '| Kicked:',
          member)
    if member is None:
        await bot.say(ctx.message.author.mention + ": Schöner Scherz!")
    elif member.id == ctx.message.author.id:
        await bot.say(ctx.message.author.mention + ": Du kannst dich nicht selber kicken!")
    elif member.id == "484382176180305950":
        await bot.say(ctx.message.author.mention + ": Ich kick mich nicht selbst!")
    else:
        await bot.kick(member)
        await bot.say(member.mention + " wurde von " + ctx.message.author.mention + "***gekickt!***")


@kick.error
async def kick_error(ctx, error):
    await bot.say('User nicht gefunden :bangbang:')


# ------------------------------
# Ban Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None):
    banner = ctx.message.author
    members = ctx.message.server.members
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Bann-Command executed! By:', banner, '| Banned:',
          member)
    if member is None:
        await bot.say(ctx.message.author.mention + ": Schöner Scherz!")
    elif member.id == ctx.message.author.id:
        await bot.say(ctx.message.author.mention + ": Du kannst dich nicht selber bannen!")
    elif member.id == "484382176180305950":
        await bot.say(ctx.message.author.mention + ": Ich bann mich nicht selbst!")
    else:
        await bot.ban(member)
        await bot.say(member.mention + " wurde von " + ctx.message.author.mention + "***gebannt!***")


@ban.error
async def ban_error(ctx, error):
    await bot.say('User nicht gefunden :bangbang:')


# ------------------------------
# Ping Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def ping(ctx):
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Ping-Command executed! By:', executer)
    before = time.monotonic()
    await bot.delete_message(ctx.message)
    ping = (time.monotonic() - before) * 1000
    await bot.say(content=f"Bot läuft bei: `{int(ping)}ms`")
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), f'Ping {int(ping)}ms')


# ------------------------------
# Commands Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def commands(ctx, ):
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Commands-Command executed! By:', executer)
    emb = discord.Embed(color=discord.Color.dark_orange(), description="Meine Befehle:")
    emb.add_field(name="ping:", value="Ping des Bots", inline=True)
    emb.add_field(name="info:", value="Info über die 218.", inline=True)
    emb.add_field(name="kick:", value=" Kickt ein User", inline=True)
    emb.add_field(name="ban:", value="Bannt ein User", inline=True)
    emb.add_field(name="wolfbot:", value="Info über mich", inline=True)
    emb.add_field(name="commands:", value="Meine Befehle", inline=True)
    emb.add_field(name="say:", value="Sende dein Text", inline=True)
    emb.add_field(name="vanish:", value="Lösche Nachricht(en)", inline=True)
    emb.add_field(name="kill:", value="Wenn soll ich töten?", inline=True)
    emb.add_field(name="yoda:", value="Yoda-Weisheiten", inline=True)
    emb.add_field(name="servers:", value="Wieviel Server benutzen mich", inline=True)
    emb.add_field(name="profile:", value="User Infos", inline=True)
    emb.add_field(name="choose:", value="Wählt aus verschiedenen Begriffen", inline=True)
    emb.add_field(name="bitcoin:", value="Zeigt den aktuellen Bitcoin Wert", inline=True)
    emb.add_field(name="discordversion:", value="Zeigt die aktuelle Discord Version", inline=True)
    emb.set_footer(text="Missbraucht sie ja nicht!")
    await bot.say(embed=emb)


# ------------------------------
# Servers Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def servers(ctx):
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Servers-Command executed! By:', executer)
    servers = list(bot.servers)
    await bot.say("[" + str(len(bot.servers)) + "] Server nutzen mich aktuell!")


# ------------------------------
# Info Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def info(ctx, ):
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Info-Command executed! By:', executer)
    embed = discord.Embed(title="Division Information", color=discord.Color.dark_green(),
                          description="Infos über die 218.Gaming Division")
    embed.add_field(name="Owner:", value="TheLonelyWolf")
    embed.add_field(name="Gründungsdatum:",
                    value="__***Die 218.Gaming Division wurde am 20. Juni 2018 von TheLonelyWolf gegründet!***__")
    await bot.say(embed=embed)


token = os.environ.get("TOKEN")
bot.run(token)
