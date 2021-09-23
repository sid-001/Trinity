import discord
import asyncio
import datetime
from discord.ext import commands
import wikipedia
import json

s_admin = 858195823296905256


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

@client.command()
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

@client.command()
async def register(ctx):
        a_dict = {f'{str(ctx.author.id)}': 86400}
        with open('main.json') as f:
            data = json.load(f)
        if str(ctx.author.id) not in data:
            data.update(a_dict)
            with open('main.json', 'w') as f:
                json.dump(data, f)
            await ctx.reply("You're now registred, you got `86,400` coins.")
        else:
            await ctx.reply("You already have an account.")

@client.command()
async def bal(ctx):
    try:
        idd= str(ctx.author.id)
        with open('main.json') as data_file:    
            data = json.load(data_file)
            aid = str(ctx.author.id)
        embed=discord.Embed(title= f"{ctx.author.name}'s balance", color=0x0FFFF)
        embed.set_thumbnail(url="https://i.imgur.com/uZIlRnK.png")
        embed.add_field(name=f"{cbn(data[aid])}", value="\u200b")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text = "Economy")
        await ctx.send(embed=embed)
    except:
        await ctx.reply("You're not registered yet!")

@client.command()
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

@client.command()
async def ping(ctx):
    await ctx.send('Pong! `{0}ms`'.format(round(client.latency, 1)))

@client.command()
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
        

@client.command()
async def say(ctx,*, content):
    await ctx.message.delete()
    await ctx.send(f"{content}")

@client.command()
async def resend(ctx):
    try:
        await ctx.message.delete()
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await ctx.send(message.content)

    except Exception as e:
        print(e)
        await ctx.send("I can't send this again!")

@client.command()
async def superuser(ctx):
    if (ctx.author.id == s_admin):
        
        msg = await ctx.send("Please enter your `ID` you've 5 seconds to reply.")
            
        try:
            message = await client.wait_for('message', check = lambda m: m.author == ctx.author and m.channel==ctx.channel,timeout = 5) 
        
        except asyncio.TimeoutError:
            await msg.edit(content="Time up!")
        
        else:
            if (message.content.lower() == "id2317"):
                await msg.edit(content="Master Controls initiated.")
                client.Superuser = True
            else:
                await msg.edit(content="This id isn't found in my database.")
    else:
        await ctx.reply(content="You don't have permission to use this command!")

@client.command()
async def disable_superuser(ctx):
    if ctx.author.id == s_admin:
        client.Superuser = False
        await ctx.reply("Superuser Changed to `Disable`")
    else:
        await ctx.reply("Superuser isn't a joke, not everyone can use it!")

@client.command()
async def dm(ctx, member: discord.Member, *, content):

    try:
        channel = await member.create_dm()
        embed = discord.Embed(title= f"{ctx.author.name}'s message",description= f"{content}", color=0x0FFFF)
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed = embed)
        await ctx.reply("Message sent successfully!")

    except:
        await ctx.reply("Can't send your message!")

@client.command(name="id")
async def id(ctx, user: discord.User):
    await ctx.send(user.id)

@client.command()
async def Sleep(ctx):
    await ctx.reply(f"Disconnected from the server.")

@client.command() 
async def add(ctx,a:int,b:int): 
    await ctx.send(f"{a} + {b} = {a+b}") 

@client.command() 
async def sub(ctx,a:int,b:int): 
    await ctx.send(f"{a} - {b} = {a-b}") 

@client.command() 
async def multiply(ctx,a:int,b:int): 
    await ctx.send(f"{a} X {b} = {a*b}") 

@client.command() 
async def divide(ctx,a:int,b:int): 
    await ctx.send(f"{a} / {b} = {a/b}") 

@client.command()
async def info(ctx,*,query):
    if query == "Siddhartha Gaur":
        await ctx.reply("Greatest person alive!")
    else:
        try:
            m = await ctx.reply(f"Collecting data from servers about `{query}` ")
            results = wikipedia.summary(query, sentences = 2)
            await m.edit(content=f"{results}")
        except Exception as e:
            await m.edit(content=f"{e}")


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=1):
    try:
        await ctx.channel.purge(limit=amount+1)
    except:
        await ctx.reply("Because of Discord limitations I can't delete messages past 2 weeks.")
        
@client.command()
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
