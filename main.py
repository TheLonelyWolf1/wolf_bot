import os

import discord
import discord.ext
from discord.ext import commands
import datetime
import asyncio
import random
import traceback

from pip._internal.utils import logging

import SECRETS
import STATICS
from boto.s3.connection import S3Connection

bot = commands.Bot(command_prefix=STATICS.PREFIX, description=" ")
bot_version = "0.1.2"
killResponses = ("%s ist aus Versehen in die Lave geschupst worden. UPS",
                 "%s ist auf ein Wolf gestoßen, danach hörte man nichts mehr von ihm.",
                 "Ich habe %s mal um die Ecke gebracht, kam alleine zurück.",
                 "Hat wer %s gesehen? War vorher mit ihm am Fluss.",
                 "Ich habe %s vergiftet. Wer möchte einen sterbenden %s sehen?",
                 "Habe %s 's Kopf weggerissen und in Mülleimer geworfen.",
                 "%s findet sein Gehirn nichtmehr. *Psst! Ich habs zerschrettert, sag es aber niemanden*",
                 "Sorry %s, aber ich musste dich leider erschießen.")

# ------------------------------
# On_Ready Output
# ------------------------------
# ------------------------------


@bot.event
async def on_ready():
    print("------------Eingeloggt--------------")
    print("Bot Name: " + bot.user.name)
    print("Bot ID: " + bot.user.id)
    print("BOT Version: " + bot_version)
    print("Discord Version: " + discord.__version__)
    print("Datum: " + datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"))
    servers = list(bot.servers)
    print("Connected on '" + str(len(bot.servers)) + "' servers:")
    for x in range(len(servers)):
        print('  ' + servers[x - 1].name)
    print("------------------------------------")
    bot.loop.create_task(status_task())

# ------------------------------
# Playing Status
# ------------------------------
# ------------------------------


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
        await bot.change_presence(game=discord.Game(name='*commands for help!'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='with Discord.py'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='with nobody'))
        await asyncio.sleep(20)
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), "Restarting RP-Cycle...")

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
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return

    if member.id == "300329919614025728":
        await bot.say(ctx.message.author.mention + ": Mich kann man nicht töten! Ich bin der Tod! :knife: ")
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), "Antwort 1 gewählt")
    elif member.id == "300329919614025728" and ctx.message.author.id == "261179915892686849":
        await bot.say(ctx.message.author.mention + ": Ich möchte dich aber nicht töten, Meister!")
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), "Antwort 2 gewählt")
    elif member.id == "261179915892686849":
        await bot.say(ctx.message.author.mention + ": Ich töte meinen Meister nicht!")
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), "Antwort 3 gewählt")
    elif member.id == ctx.message.author.id:
        await bot.say(ctx.message.author.mention * ": Du kannst auch Selbstmord betreiben. Dann mach ich mir die Hände nicht schmutzig!")
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), "Antwort 4 gewählt")
    else:
        choice = killResponses[random.randrange(0, len(killResponses))] % member.mention
        await bot.say(ctx.message.author.mention + ": " + choice)

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
# Add Trainee Command
# ------------------------------
# ------------------------------


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def addtrainee(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="≗Trainee")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'AddTrainee-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role, ' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "≗Trainee" in role_names:
        await bot.say(member.mention + " besitzt schon das Amt eines Trainees!")
        return
    else:
        await bot.add_roles(user, role)
        await bot.say(member.mention + " ist nun ein ***Trainee*** | Willkommen im Team!")


# ------------------------------
# Add Mod Command
# ------------------------------
# ------------------------------


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def addmod(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="≘Moderators")
    delrole = discord.utils.get(user.server.roles, name="≗Trainee")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'AddMod-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role ,' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "≘Moderators" in role_names:
        await bot.say(member.mention + " besitzt schon das Amt eines Moderators!")
        return
    else:
        await bot.add_roles(user, role)
        await bot.say(member.mention + " ist nun ein ***Moderator*** | Willkommen im Team!")
        if "≗Trainee" in role_names:
            await bot.remove_roles(user, delrole)
            print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), member, "'s Trainee-Role entfernt!")
        else:
            print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), member, "hat kein Trainee Rang gehabt")

# ------------------------------
# Add SteamMod Command
# ------------------------------
# ------------------------------


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def addsmod(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="Steam-Mods")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Addsmod-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role, ' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "≗Trainee" in role_names:
        await bot.say(member.mention + " besitzt schon das Amt eines Steam-Mod!")
        return
    else:
        await bot.add_roles(user, role)
        await bot.say(member.mention + " ist nun ein ***Steam-Mod*** | Willkommen im Team!")


# ------------------------------
# Add Admin Command
# ------------------------------
# ------------------------------


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def addadmin(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="≜Administrators")
    delrole = discord.utils.get(user.server.roles, name="≘Moderators")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Addadmin-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role, ' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "≜Administrators" in role_names:
        await bot.say(member.mention + " besitzt schon das Amt eines Administrators!")
        return
    else:
        await bot.add_roles(user, role)
        await bot.say(member.mention + " ist nun ein ***Administrator*** | Willkommen im Team!")
        if "≘Moderators" in role_names:
            await bot.remove_roles(user, delrole)
            print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), member, "'s Mod-Role entfernt!")
        else:
            print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), member, "hat kein Mod Rang gehabt")


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def addsadmin(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="Steam-Admins")
    delrole = discord.utils.get(user.server.roles, name="Steam-Mods")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Addsadmin-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role, ' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "≗Trainee" in role_names:
        await bot.say(member.mention + " besitzt schon das Amt eines Steam-Admin!")
        return
    else:
        await bot.add_roles(user, role)
        await bot.say(member.mention + " ist nun ein ***Steam-Admin*** | Willkommen im Team!")
        if "Steam-Mods" in role_names:
            await bot.remove_roles(user, delrole)
            print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), member, "'s SteamMod-Role entfernt!")
        else:
            print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), member, "hat kein SteamMod Rang gehabt")


# ------------------------------
# Remove Mod Command
# ------------------------------
# ------------------------------


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def rmod(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="≘Moderators")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'RemoveMod-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role ,' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "≘Moderators" in role_names:
        await bot.remove_roles(user, role)
        await bot.say(member.mention + " ist nun kein Moderator mehr!")
        return
    else:
        await bot.add_roles(user, role)
        await bot.say(member.mention + " hat dieses Amt nicht!")


# ------------------------------
# Remove SMod Command
# ------------------------------
# ------------------------------


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def rsmod(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="Steam-Mods")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'RemoveMod-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role ,' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "Steam-Mods" in role_names:
        await bot.remove_roles(user, role)
        await bot.say(member.mention + " ist nun kein Steam-Moderator mehr!")
        return
    else:
        await bot.add_roles(user, role)
        await bot.say(member.mention + " hat dieses Amt nicht!")
# ------------------------------
# Remove Admin Command
# ------------------------------
# ------------------------------


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def radmin(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="≜Administrators")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Removeadmin-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role, ' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "≜Administrators" in role_names:
        await bot.remove_roles(user, role)
        await bot.say(member.mention + " ist nun kein Administrator mehr!")
        return
    else:
        await bot.say(member.mention + " hat dieses Amt nicht!")


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def rsadmin(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="Steam-Admins")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Removeadmin-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role, ' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "Steam-Admins" in role_names:
        await bot.remove_roles(user, role)
        await bot.say(member.mention + " ist nun kein Steam-Administrator mehr!")
        return
    else:
        await bot.say(member.mention + " hat dieses Amt nicht!")

# ------------------------------
# Remove Trainee Command
# ------------------------------
# ------------------------------


@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
@bot.command(pass_context=True)
async def rtrainee(ctx, *, member: discord.Member = None):
    user = member
    role = discord.utils.get(user.server.roles, name="≗Trainee")
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'RemoveTrainee-Command executed! By:', executer)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), role, ' : ', user)
    role_names = [role.name for role in member.roles]
    if member is None:
        await bot.say(ctx.message.author.mention + ": Ich kann das VOID nicht töten!")
        return
    if member.mention == ctx.message.author.mention:
        await bot.say(ctx.message.author.mention + ": Bitte lass dich von jemanden anderen ernennen!")
    elif "≗Trainee" in role_names:
        await bot.remove_roles(user, role)
        await bot.say(member.mention + " ist nun kein Administrator mehr!")
        return
    else:
        await bot.add_roles(user, role)
        await bot.say(member.mention + " hat dieses Amt nicht!")




# ------------------------------
# Kick Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None):
    kicker = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Kick-Command executed! By:', kicker, '| Kicked:',member)
    if member is None:
        await bot.say(ctx.message.author.mention + ": Schöner Scherz!")
    elif member.id == ctx.message.author.id:
        await bot.say(ctx.message.author.mention + ": Du kannst dich nicht selber kicken!")
    elif member.id == "300329919614025728":
        await bot.say(ctx.message.author.mention + ": Ich kick mich nicht selbst!")
    else:
        await bot.kick(member)
        await bot.say(member.mention + " wurde von " + ctx.message.author.mention + "***gekickt!***")

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
        print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Bann-Command executed! By:', banner, '| Banned:', member)
        if member is None:
            await bot.say(ctx.message.author.mention + ": Schöner Scherz!")
        elif member.id == ctx.message.author.id:
            await bot.say(ctx.message.author.mention + ": Du kannst dich nicht selber bannen!")
        elif member.id == "300329919614025728":
            await bot.say(ctx.message.author.mention + ": Ich bann mich nicht selbst!")
        else:
            await bot.ban(member)
            await bot.say(member.mention + " wurde von " + ctx.message.author.mention + "***gebannt!***")

# ------------------------------
# Ping Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def ping(ctx,):
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Ping-Command executed! By:', executer)
    await bot.say( embed=discord.Embed(color=discord.Color.dark_blue(), description="PONG!"))

# ------------------------------
# Commands Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def commands(ctx,):
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
    emb.add_field(name="kill:", value="Wenn soll ich töten?")
    emb.add_field(name="add(s)mod,(s)admin:", value="Füge Leute dem Team zu")
    emb.add_field(name="remove(s)mod,(s)admin:", value="Entferne Leute vom Team")
    emb.set_footer(text="Missbraucht sie ja nicht!")
    await bot.say(embed=emb)

# ------------------------------
# Info Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def info(ctx,):
    executer = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Info-Command executed! By:', executer)
    embed = discord.Embed(title="Division Information",color=discord.Color.dark_green(), description="Infos über die 218.Gaming Division")
    embed.add_field(name="Owner:", value="TheLonelyWolf")
    embed.add_field(name="Gründungsdatum:", value="__***Die 218.Gaming Division wurde am 20. Juni 2018 von TheLonelyWolf gegründet!***__")
    await bot.say(embed=embed)

s3 = S3Connection(os.environ['414141244441'], os.environ['wolf313122'])
bot.run(s3)
