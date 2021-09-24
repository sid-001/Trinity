import discord
import asyncio
import datetime
from discord.ext import commands
import wikipedia
import json
import pymongo

s_admin = 858195823296905256
myclient = pymongo.MongoClient("mongodb+srv://SidDB:iqYEMReHesQ0pNAJ@sidbot.81mkh.mongodb.net/retryWrites=true&w=majority")
mydb = myclient["Trinity"]
mycol = mydb["Userinfo"]


def cbn(bal):
    res = (format (bal, ','))
    return(str(res))

def get_prefix(client, message): 
    with open('prefixes.json', 'r') as f: 
        prefixes = json.load(f) 
    return prefixes[str(message.guild.id)]


client = commands.Bot(
    command_prefix= (get_prefix),
    )

print(get_prefix)

client.Superuser = False
client.spam = True

@client.event
async def on_ready():
    print("We're ready!")
@client.event
async def on_guild_join(guild): 
    with open('prefixes.json', 'r') as f: 
        prefixes = json.load(f) 

    prefixes[str(guild.id)] = '$'

    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4) 

@client.event
async def on_guild_remove(guild): 
    with open('prefixes.json', 'r') as f: 
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) 

    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4)

@client.command(brief='For changing the prefix')
async def prefix(ctx, prefix="$"):
    if ctx.author.id == s_admin and client.Superuser:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'The new prefix for this server is `{prefix}`') 
    elif ctx.author.id == s_admin and client.Superuser == False:
        await ctx.reply("Use `Master Controls` to use this command.")
    else:
        await ctx.reply("You're not authorised to use this command.")

@client.command(brief='Register yourself tro Trinity Economy commands')
async def register(ctx):
    user = mycol.find_one({"id": ctx.author.id})
    if user == None:
        userinfo = {
        "name": ctx.author.name,
        "id": ctx.author.id,
        "balance": 86400
        }
        mycol.insert_one(userinfo)
        embed=discord.Embed(title="Registered Successfully.", color=0xFF0000)
        await ctx.reply(embed=embed)
    else:
        embed=discord.Embed(title="You're already registered.", color=0xFF0000)
        await ctx.reply(embed=embed)

@client.command(brief='Shows you current balance')
async def bal(ctx):
    user = mycol.find_one({"id":ctx.author.id})
    if user == None:
        embed=discord.Embed(title="You're not registered yet.", color=0xFF0000)
        await ctx.reply(embed=embed)
    else:
        embed=discord.Embed(title= f"{ctx.author.name}'s balance", color=0xFF0000)
        embed.set_thumbnail(url="https://i.imgur.com/uZIlRnK.png")
        embed.add_field(name= f"{cbn(user['balance'])}", value="\u200b")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text = "Economy")
        await ctx.send(embed=embed)

@client.command(brief='Update your balance to as much you want')
async def updatebal(ctx, a=100000):
    if ctx.author.id == s_admin and client.Superuser:
        data = {str(ctx.author.id):a}
        with open('main.json', 'w') as f:
            json.dump(data, f)
        await ctx.reply(f"Your new balance is `{cbn(a)}`")
    elif ctx.author.id == s_admin and client.Superuser == False:
        await ctx.reply("Use `Master Controls` to use this command.")
    else:
        await ctx.reply("You're not authorised to use this command.")

@client.command(brief='Shows bot response time')
async def ping(ctx):
    await ctx.send('Pong! `{0}ms`'.format(round(client.latency, 1)))

@client.command(brief='Spams as much as 30 times')
async def spam(ctx, a:int,*,cont):
    if client.spam:
        if a > 30:
            await ctx.reply("Can't spam more than 30 times.")
        else:
            await ctx.send(f"spamming {a} times as {cont}")
            for x in range(a):
                await ctx.send(f"{cont}")
    else:
        await ctx.reply("command is disabled")
        

@client.command(brief='Says your message')
async def say(ctx,*, content):
    await ctx.message.delete()
    await ctx.send(f"{content}")

@client.command(brief='Resends the message you replied for')
async def resend(ctx):
    try:
        await ctx.message.delete()
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await ctx.send(message.content)

    except Exception as e:
        print(e)
        await ctx.send("I can't send this again!")

@client.command(brief='Gives you full access to the system')
async def root(ctx):
    if (ctx.author.id == s_admin):
        if client.Superuser:
            client.Superuser=False
            embed = discord.Embed(title=f"Superuser Disabled", color=0xFF0000)
            await ctx.reply(embed=embed)
        else:
            client.Superuser=True
            embed = discord.Embed(title=f"Superuser Enabled", color=0xFF0000)
            await ctx.reply(embed=embed)
    else:
            embed = discord.Embed(title=f"You're not authorised to use this command.", color=0xFF0000)
            await ctx.reply(embed=embed)


@client.command(brief='DM your message to the mentioned user')
async def dm(ctx, member: discord.Member, *, content):

    try:
        channel = await member.create_dm()
        embed = discord.Embed(title= f"{ctx.author.name}'s message",description= f"{content}", color=0x0FFFF)
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed = embed)
        await ctx.reply("Message sent successfully!")

    except:
        await ctx.reply("Can't send your message!")

@client.command(brief='Shows ID of mentioned user')
async def id(ctx, user: discord.User):
    await ctx.send(user.id)


@client.command(brief='Add two numbers') 
async def add(ctx,a:int,b:int): 
    await ctx.send(f"{a} + {b} = {a+b}") 

@client.command(brief='subtract two numbers') 
async def sub(ctx,a:int,b:int): 
    await ctx.send(f"{a} - {b} = {a-b}") 

@client.command(brief='Multiply two numbers') 
async def multiply(ctx,a:int,b:int): 
    await ctx.send(f"{a} X {b} = {a*b}") 

@client.command(brief='Divide two numbers') 
async def divide(ctx,a:int,b:int): 
    await ctx.send(f"{a} / {b} = {a/b}") 


@client.command(brief='Gives information about query')
async def info(ctx,*,query):
    if query == "Siddhartha Gaur":
        await ctx.reply("Greatest person alive!")
    elif query == "Riya":
        await ctx.reply("Bhagwan Jaane:smiling_face_with_tear:")
    else:
        try:
            m = await ctx.reply(f"Collecting data from servers about `{query}` ")
            results = wikipedia.summary(query, sentences = 2)
            embed = discord.Embed(title=f"Results for **{query}**", description=f"{results}", color=0xFF0000)
            await m.delete()
            await ctx.reply(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="**Something went wrong**", description=f"{e}", color=0xFF0000)
            await m.delete()
            await ctx.reply(embed=embed)


@client.command(brief='Clear messages')
async def clear(ctx, amount=1):
    if client.Superuser:
        try:
            await ctx.channel.purge(limit=amount+1)
        except:
            await ctx.reply("An unknown error occured")
    else:
        await ctx.reply("Use `Master Controls` to execute command.")   
        
@client.command(brief='Enable/Disable commands')
async def toggle(ctx, command=None):
    if client.Superuser: 
        if command == "spam":
            if client.spam == False:
                client.spam = True
                await ctx.reply("Command Enabled")
            else:
                client.spam = False
                await ctx.reply("Command Disabled")
        else:
            await ctx.reply("Unknown Command ID")
    else:
        await ctx.reply("Use `Master Controls` to execute this command.")
           
client.run('ODg5MzY4NDQ2MTkyNzM0MjA5.YUgO6Q.uBYG00vvUjk4mXXAlZvrsLvGZEU')
