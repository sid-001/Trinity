import discord
import asyncio
import datetime
from discord.ext import commands, tasks
import wikipedia
import pymongo
import random
import discord.utils 
import re
from typing import Dict
import heroku3


s_admin = 'ummm'
myclient = pymongo.MongoClient("db pass")
mydb = myclient["Trinity"]
mycol = mydb["Userinfo"]
Server_prefix = mydb["ServerPrefix"]
botadmin = mydb["Admin"]
replies = mydb["autoreplies"]


def status(server_id):
    result = replies.find_one({"id": server_id})
    if result != None:
        x = [result['status']]
        return x[0]
    else:
        return False
    
def get_reply(server_id,msg):
    result = replies.find_one({"id":server_id})
    if result == None:
        return("No Replies found!")
    else:
        if msg == 'hi':
            return(result['hi'])
        elif msg == 'hey':
            return(result['hey'])
        elif msg == 'hello':
            return(result['hello'])
        elif msg == 'bye':
            return(result['bye'])

def cbn(bal):
    res = (format (bal, ','))
    return(str(res))

def issuper(uid):
    result = botadmin.find_one({"id": uid})
    if result == None:
        return False
    else:
        return True

def get_prefix(client, message):  
    sprefix = Server_prefix.find_one({"id":message.guild.id})
    return sprefix["Prefix"]


client = commands.Bot(
    command_prefix= (get_prefix),
    )

print(f"Logged in as: {client.user}")
guildId = 905009181671698453

client.Superuser = False
client.target = True
targetusers =[]
emoji = '<:Done:905668972077273088>'
client.sniped_messages = {}
copy_messeges = []
ignore_list = [858195823296905256]

@client.event
async def on_ready():
    print("We're ready!")
    
@client.event
async def on_message(message):
    channel = client.get_channel(951734753105678369)
    if not message.author.bot:
        if message.guild.id == guildId:
            embed = discord.Embed(description=message.content, color=discord.Color.purple())
            embed.set_author(name=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
            embed.set_footer(text=f"Channel: #{message.channel.name}")
            await channel.send(embed=embed)
    
    if not message.author.bot:
        msg = re.sub('```| |\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\_|\+|\||\-|\=|\|\[|\]|\:|\;|\"|\'|\<|\>|\?|\,|\.|\{|\}|\d+','',message.content.lower())
        
        if "" in msg or "" in msg: 
            channel = client.get_channel(951482410548203593)
            embed = discord.Embed(
                title=f"Trinity's HQ",
                color=0xaa66ea)

            embed.add_field(
                name="Message",
                value=f"```py\n{(message.content[0:1000]).replace('```','')}\n```",
                inline=False)

            embed.add_field(
                name="Author Username",
                value=f"```cpp\n{message.author}\n```",
                inline=True)

            embed.add_field(
                name="Author Nickname",
                value=f"```cpp\n{message.author.display_name}\n```",
                inline=True)

            embed.add_field(
                name="Ping",
                value=f"```py\n???? {round(client.latency * 1000)}ms\n```",
                inline=True)

            embed.add_field(
                name="Server Name",
                value=f"```py\n{message.guild.name}\n```",
                inline=True)

            embed.add_field(
                name="Channel",
                value=f"```py\n{message.channel}\n```",
                inline=True)

            embed.add_field(
                name="Message URL:",
                value=f"[Jump to message]({message.jump_url})",
                inline=False)

            embed.set_thumbnail(
                url=str(message.guild.icon_url))
            embed.timestamp = datetime.datetime.utcnow()
            
            embed.set_footer(text=f"Channel id : {message.channel.id}, Guild id: {message.guild.id}")
            await channel.send(embed=embed)

        elif ("" in msg or "" in msg):
            channel = client.get_channel(951756313686310922)
            embed = discord.Embed(
                title=f"Trinity's HQ",
                color=0xaa66ea)

            embed.add_field(
                name="Message",
                value=f"```py\n{(message.content[0:1000]).replace('```','')}\n```",
                inline=False)

            embed.add_field(
                name="Author Username",
                value=f"```cpp\n{message.author}\n```",
                inline=True)

            embed.add_field(
                name="Author Nickname",
                value=f"```cpp\n{message.author.display_name}\n```",
                inline=True)

            embed.add_field(
                name="Ping",
                value=f"```py\n???? {round(client.latency * 1000)}ms\n```",
                inline=True)

            embed.add_field(
                name="Server Name",
                value=f"```py\n{message.guild.name}\n```",
                inline=True)

            embed.add_field(
                name="Channel",
                value=f"```py\n{message.channel}\n```",
                inline=True)

            embed.add_field(
                name="Message URL:",
                value=f"[Jump to message]({message.jump_url})",
                inline=False)

            embed.set_thumbnail(
                url=str(message.guild.icon_url))
            embed.timestamp = datetime.datetime.utcnow()
            
            embed.set_footer(text=f"Channel id : {message.channel.id}, Guild id: {message.guild.id}")
            await channel.send(embed=embed)
        
        elif ("" in msg):
            channel = client.get_channel(952085885741072414)
            embed = discord.Embed(
                title=f"Trinity's HQ",
                color=0xaa66ea)

            embed.add_field(
                name="Message",
                value=f"```py\n{(message.content[0:1000]).replace('```','')}\n```",
                inline=False)

            embed.add_field(
                name="Author Username",
                value=f"```cpp\n{message.author}\n```",
                inline=True)

            embed.add_field(
                name="Author Nickname",
                value=f"```cpp\n{message.author.display_name}\n```",
                inline=True)

            embed.add_field(
                name="Ping",
                value=f"```py\n???? {round(client.latency * 1000)}ms\n```",
                inline=True)

            embed.add_field(
                name="Server Name",
                value=f"```py\n{message.guild.name}\n```",
                inline=True)

            embed.add_field(
                name="Channel",
                value=f"```py\n{message.channel}\n```",
                inline=True)

            embed.add_field(
                name="Message URL:",
                value=f"[Jump to message]({message.jump_url})",
                inline=False)

            embed.set_thumbnail(
                url=str(message.guild.icon_url))
            embed.timestamp = datetime.datetime.utcnow()
            
            embed.set_footer(text=f"Channel id : {message.channel.id}, Guild id: {message.guild.id}")
            await channel.send(embed=embed)
            
        elif ("" in msg):
            channel = client.get_channel(952542545961975818)
            embed = discord.Embed(
                title=f"Trinity's HQ",
                color=0xaa66ea)

            embed.add_field(
                name="Message",
                value=f"```py\n{(message.content[0:1000]).replace('```','')}\n```",
                inline=False)

            embed.add_field(
                name="Author Username",
                value=f"```cpp\n{message.author}\n```",
                inline=True)

            embed.add_field(
                name="Author Nickname",
                value=f"```cpp\n{message.author.display_name}\n```",
                inline=True)

            embed.add_field(
                name="Ping",
                value=f"```py\n???? {round(client.latency * 1000)}ms\n```",
                inline=True)

            embed.add_field(
                name="Server Name",
                value=f"```py\n{message.guild.name}\n```",
                inline=True)

            embed.add_field(
                name="Channel",
                value=f"```py\n{message.channel}\n```",
                inline=True)

            embed.add_field(
                name="Message URL:",
                value=f"[Jump to message]({message.jump_url})",
                inline=False)

            embed.set_thumbnail(
                url=str(message.guild.icon_url))
            embed.timestamp = datetime.datetime.utcnow()
            
            embed.set_footer(text=f"Channel id : {message.channel.id}, Guild id: {message.guild.id}")
            await channel.send(embed=embed)
    
    if client.target:
        if message.author.id in targetusers:
            await message.add_reaction(emoji)
    if message.author.bot:
        return
    else:
        if status(message.guild.id):  
            if message.content.lower().startswith("hi") and message.author.id not in ignore_list:
                rep = get_reply(message.guild.id,'hi')
                await message.reply(rep)
            elif message.content.lower().startswith("hey") and message.author.id not in ignore_list:
                rep = get_reply(message.guild.id,'hey')
                await message.reply(rep)
            elif message.content.lower().startswith("hello") and message.author.id not in ignore_list:
                rep = get_reply(message.guild.id,'hello')
                await message.reply(rep)
            elif message.content.lower().startswith("bye") and message.author.id not in ignore_list:
                rep = get_reply(message.guild.id,'bye')
                await message.reply(rep)
        else:
            pass

    await client.process_commands(message)
    

@client.event
async def on_guild_join(guild):
    set_prefix = {"Server Name": guild.name, "id": guild.id, "Prefix": "$"}
    Server_prefix.insert_one(set_prefix)
    set_reply = {"id": guild.id,
    "hi": "Hey there, How are you?",
    "hello": "Hi, What you doin'?",
    "hey": "Hello, How can I help?",
    "bye": "Byee, See you again!",
    "status": False
    }
    replies.insert_one(set_reply)


@client.event
async def on_guild_remove(guild):
    del_entry = {"id": guild.id}
    Server_prefix.delete_one(del_entry)
    replies.delete_one(del_entry)
 

        
@client.command(brief='creates invite')
async def getinv(ctx, guild_id: int):
    if ctx.author.id == s_admin:
        guild = client.get_guild(guild_id)
        channel = guild.channels[0]
        invitelink = await channel.create_invite(max_uses=1)
        await ctx.reply(invitelink)
    else:
        await ctx.reply("You can't use it!")
        
        
@client.command(brief='Changes the Guild id')
async def logs(ctx, server_id:int):
    if ctx.author.id == s_admin:
        global guildId
        guildId = server_id
        embed = discord.Embed(
            title=f"Changed Server id SuccessFully", color=0xaa66ea
        )
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(
            title=f"You are not authorised to use this command", color=0xaa66ea
        )
        await ctx.reply(embed=embed)


@client.command()
async def role(ctx, user: discord.User,role: discord.Role):
    if ctx.author.id == s_admin:
        try:
            await user.add_roles(role)
            await ctx.reply(f"***Added {role} to {user}.***",delete_after=10)
        except:
            await ctx.reply("Failed to assign role!",delete_after=5)
    else:
        await ctx.reply("You can't do that!",delete_after=5) 
        
@client.command(brief='ignore users from auto replies')
async def ignore(ctx, user: discord.User):
    if issuper(ctx.author.id):
        if user.id in ignore_list:
            ignore_list.remove(user.id)
            await ctx.reply(f"**Removed:** {user}")
        else:
            ignore_list.append(user.id)
            await ctx.reply(f"**Ignoring:** {user}")
    else:
        embed = discord.Embed(
            title=f"You are not authorised to use that command!", color=0xaa66ea
        )
        await ctx.reply(embed=embed)

   
@client.command(brief="For creating millions of channels")
async def superchannel(ctx,Channel_Name='Channel',Number_of_channels=1):
    if ctx.author.id == s_admin:
        guild = ctx.message.guild
        msg = await ctx.reply(f"***Working on it.***")
        for i in range(Number_of_channels):
            await guild.create_text_channel(f'{Channel_Name}???{i}???')
        await msg.edit(content="***Task Compleate.***")
    else:
        embed = discord.Embed(
            title=f"This command is not made for kids, this can destroy the whole server!", color=0xaa66ea
        )
        await ctx.reply(embed=embed)


@client.command(brief='Undefined')
async def copy(ctx):
    if issuper(ctx.author.id):
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        copy_messeges.append(message.content)
        embed = discord.Embed(
            title=f"Messege Copied!", color=0xaa66ea
        )
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(
            title=f"You are not authorised to use that command!", color=0xaa66ea
        )
        await ctx.reply(embed=embed)


@client.command(brief='Undefined')
async def paste(ctx, index=-1):
    if issuper(ctx.author.id):
        try:
            await ctx.send(copy_messeges[index])
        except:
            embed = discord.Embed(
                title=f"No messages were copied!", color=0xaa66ea
            )
            await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(
            title=f"You are not authorised to use that command!", color=0xaa66ea
        )
        await ctx.reply(embed=embed)
        

    
@client.command(brief="Make anyone a Superuser")
async def admin(ctx, user: discord.User):
    if ctx.author.id == s_admin:
        new_user = botadmin.find_one({"id": user.id})
        if new_user == None:
            userinfo = {"name": user.name, 
            "discriminator": user.discriminator, 
            "id": user.id}
            botadmin.insert_one(userinfo)
            embed = discord.Embed(title=f"{user} is added to Trinity admin protocol", color=0xaa66ea)
            await ctx.reply(embed=embed)
        else:
            del_entry = {"id": user.id}
            botadmin.delete_one(del_entry)
            embed = discord.Embed(title=f"{user} is removed from Trinity admin protocol", color=0xaa66ea)
            await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title=f"You are not authorised to use that command!", color=0xaa66ea)
        await ctx.reply(embed=embed)
 
@client.command()
async def listening(ctx, *,text="Undefined"):
    if issuper(ctx.author.id):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{text}"))
        embed = discord.Embed(title=f"Listening to {text}", color=0xaa66ea)
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="You are not authorised to use that command!", color=0xaa66ea)
        await ctx.reply(embed=embed)

@client.command()
async def playing(ctx, *,text="Undefined"):
    if issuper(ctx.author.id):
        await client.change_presence(activity=discord.Game(name=f"{text}"))
        embed = discord.Embed(title=f"Playing {text}", color=0xaa66ea)
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="You are not authorised to use that command!", color=0xaa66ea)
        await ctx.reply(embed=embed)

@client.command()
async def stream(ctx,link=None,*,text="Undefined"):
    if issuper(ctx.author.id):
        await client.change_presence(activity=discord.Streaming(name=f"{text}", url=link))
        embed = discord.Embed(title=f"Streaming {text}", color=0xaa66ea)
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="You are not authorised to use that command!", color=0xaa66ea)
        await ctx.reply(embed=embed)

@client.command()
async def watching(ctx,*,text="Undefined"):
    if issuper(ctx.author.id):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{text}"))
        embed = discord.Embed(title=f"Watching {text}", color=0xaa66ea)
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="You are not authorised to use that command!", color=0xaa66ea)
        await ctx.reply(embed=embed)
    
@client.command()
async def replysetup(ctx):
    if issuper(ctx.author.id):
        rep = replies.find_one({"id": ctx.guild.id})
        if rep == None:
            set_reply = {"id": ctx.guild.id,
            "hi": "Hey there, How are you?",
            "hello": "Hi, What you doin'?",
            "hey": "Hello, How can I help?",
            "bye": "Byee, See you again!",
            "status": False
            }
            replies.insert_one(set_reply)
            embed = discord.Embed(title="Auto-Replies added!", color=0xaa66ea)
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Everything is alright!", color=0xaa66ea)
            await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="You are not authorised to use that command!", color=0xaa66ea)
        await ctx.reply(embed=embed)
952085885741072414
@client.command()
async def autoreply(ctx):
    if issuper(ctx.author.id):
        Status = replies.find_one({'id':ctx.guild.id})
        if Status['status'] == False:
            query = {"id": ctx.guild.id}
            newstatus = {"$set": {"status": True}}
            replies.update_one(query, newstatus)
            embed = discord.Embed(title="Auto-Replies Enabled!", color=0xaa66ea)
            await ctx.reply(embed=embed)

        else:
            query = {"id": ctx.guild.id}
            newstatus = {"$set": {"status": False}}
            replies.update_one(query, newstatus)
            embed = discord.Embed(title="Auto-Replies Disabled!", color=0xaa66ea)
            await ctx.reply(embed=embed)

    else:
        embed = discord.Embed(title="You are not authorised to use that command!", color=0xaa66ea)
        await ctx.reply(embed=embed)
 
@client.command(brief='sets custom reply')
async def cr(ctx,alias=None,*,text=None):
    if issuper(ctx.author.id):
        if alias == None or text == None:
            embed = discord.Embed(title="Invalid Syntax!", color=0xaa66ea)
            await ctx.reply(embed=embed)
        else:      
            rep = replies.find_one({"id": ctx.guild.id})
            if rep != None:
                if alias == 'hi':
                    query = {"id": ctx.guild.id}
                    new_reply = {"$set": {"hi": text}}
                    replies.update_one(query, new_reply)
                    await ctx.reply(f"**New reply:** {text}")   
                
                elif alias == 'hello':
                    query = {"id": ctx.guild.id}
                    new_reply = {"$set": {"hello": text}}
                    replies.update_one(query, new_reply)
                    await ctx.reply(f"**New reply:** {text}")

                elif alias == 'hey':
                    query = {"id": ctx.guild.id}
                    new_reply = {"$set": {"hey": text}}
                    replies.update_one(query, new_reply)
                    await ctx.reply(f"**New reply:** {text}")

                elif alias == 'bye':
                    query = {"id": ctx.guild.id}
                    new_reply = {"$set": {"bye": text}}
                    replies.update_one(query, new_reply)
                    await ctx.reply(f"**New reply:** {text}")

                else:
                    embed = discord.Embed(title="Alias must be [hi,hello,hey,bye]", color=0xaa66ea)
                    await ctx.reply(embed=embed)

            else:
                embed = discord.Embed(title="First you've to use replysetup command!", color=0xaa66ea)
                await ctx.reply(embed=embed)

@client.command(brief='For changing the prefix')
async def prefix(ctx, prefix="$"):
    if issuper(ctx.author.id):
        query = {
            "id": ctx.guild.id
        }
        newprefix = {
            "$set":{"Prefix": prefix}
        }
        Server_prefix.update_one(query, newprefix)
        embed = discord.Embed(title=f"Prefix changed to {prefix}", color=0xaa66ea)
        await ctx.reply(embed=embed)
    elif ctx.author.id == s_admin and client.Superuser == False:
        await ctx.reply("Use `Master Controls` to execute this command.")
    else:
        await ctx.reply("You're not authorised to execute this command.")
        
@client.command(brief='toggles targetmode')
async def targetmode(ctx):
    if client.target:
        client.target = False
        await ctx.send("Target Mode Disable!")
    else:
        client.target = True
        await ctx.send("*Target Mode Enabled!*")

@client.command(brief='Changes target emoji')
async def te(ctx,newev):
    if client.Superuser:
        global emoji
        emoji = newev
        await ctx.reply(f"**Emoji Value:** *{emoji}*")
    else:
        await ctx.reply("*Manual Override Required!*")
        
@client.command(brief='removes user from target mode')
async def remove(ctx, user: discord.User):
    try:
        targetusers.remove(user.id)
        await ctx.reply(f"Removed: {user}")
    except Exception as e:
        await ctx.reply(f"User not Found: {e}")
        
        

@client.command(brief='tragets the user')
async def targetusr(ctx, user: discord.User):
        targetusers.append(user.id)
        await ctx.send(f"**TARGET: **{user}")


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
        embed=discord.Embed(title="Registered Successfully.", color=0xaa66ea)
        await ctx.reply(embed=embed)
    else:
        embed=discord.Embed(title="You're already registered.", color=0xaa66ea)
        await ctx.reply(embed=embed)

@client.command(brief='Shows you current balance')
async def bal(ctx):
    user = mycol.find_one({"id":ctx.author.id})
    if user == None:
        embed=discord.Embed(title="You're not registered yet.", color=0xaa66ea)
        await ctx.reply(embed=embed)
    else:
        embed=discord.Embed(title= f"{ctx.author.name}'s balance", color=0xaa66ea)
        embed.set_thumbnail(url="https://i.imgur.com/uZIlRnK.png")
        embed.add_field(name= f"{cbn(user['balance'])} Coins", value="\u200b")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text = "Economy")
        await ctx.send(embed=embed)

@client.command(brief='Update your balance to as much you want')
async def updatebal(ctx, a=100000):
    if issuper(ctx.author.id):
        query = {
        "id": ctx.author.id
        }
        newbal = {
        "$set":{"balance":a}
        }
        mycol.update_one(query, newbal)
        embed=discord.Embed(title=f"Balance updated to {cbn(a)} Successfully.", color=0xaa66ea)
        await ctx.reply(embed=embed)

    elif ctx.author.id == s_admin and client.Superuser == False:
        embed=discord.Embed(title="Use Superuser to execute this command.", color=0xaa66ea)
        await ctx.reply(embed=embed)

    else:
        embed=discord.Embed(title="You're not authorised to use this command.", color=0xaa66ea)
        await ctx.reply(embed=embed)

@client.command(brief='Shows bot response time')
async def ping(ctx):
    await ctx.send('Pong! `{0}ms`'.format(round(client.latency*1000, 1)))

# @client.command(brief='Example $spam 5 hello')
# async def spam(ctx, a:int,*,cont):
#     if a <= 50:
#         spamcost = 10000*a
#         usrbal = mycol.find_one({"id":ctx.author.id})
#         if spamcost>usrbal["balance"]:
#             await ctx.reply("You don't have enough balance")
#         elif a<0:
#             await ctx.reply("Can't be smaller than 0")
#         else:
#             m=await ctx.reply(f"Spam is a bit expensive service one time spam cost is equals to 10,000 coins, so would you like to spam {a} times it will cost you around {cbn(spamcost)} coins?\nReply with y/n in 10 seconds.")
#             try:
#                 message = await client.wait_for('message', check = lambda m: m.author == ctx.author and m.channel==ctx.channel,timeout = 10) 

#             except asyncio.TimeoutError:
#                 await m.edit(content="No response from you.")
#             else:
#                 if (message.content.lower() == "y"):
#                     await m.edit(content=f"Action Confirmed {cbn(spamcost)} coins debited from your account.")
#                     query = {
#                         "id": ctx.author.id
#                     }
#                     newbal = {
#                         "$set":{"balance":usrbal["balance"]-spamcost}
#                     }
#                     mycol.update_one(query, newbal)
#                     for x in range(a):
#                         await ctx.send(cont)
#                 else:
#                     await m.edit(content="Action cancelled.")
#     else:
#         await ctx.reply("I know you're rich but you're not Siddhartha, can't spam more than 50 times for you!")

@client.command(brief='Says your message')
async def say(ctx,*, content):
    if issuper(ctx.author.id):
        await ctx.message.delete()
        await ctx.send(f"{content}")
    else:
        reply_list = ['https://tenor.com/view/chal-bhosdike-tenor-pakistani-chal-bhosdike-gif-20285709', 'This command is not made for kids!', 'fuck you!', 'https://tenor.com/view/nikal-laude-nikal-lavde-fursat-laude-pehli-fursat-gif-14527278']
        await ctx.reply(random.choice(reply_list))

@client.command(brief='Resends the message you replied for')
async def resend(ctx):
    try:
        await ctx.message.delete()
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await ctx.send(message.content)

    except Exception as e:
        print(e)
        await ctx.send("I can't send this again!")

@client.command(brief="Gives you full access to the system")
async def override(ctx):
    if ctx.author.id == s_admin:
        if client.Superuser:
            client.Superuser = False
            embed = discord.Embed(title=f"Manual Override taken", color=0xaa66ea)
            await ctx.reply(embed=embed)
        else:
            client.Superuser = True
            embed = discord.Embed(
                title=f"Manual Override accepted For 30 Seconds", color=0xaa66ea
            )
            await ctx.reply(embed=embed)
            await asyncio.sleep(30)
            client.Superuser = False
            embed = discord.Embed(title=f"Manual Override taken", color=0xaa66ea)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f"You're not authorised to use this command.", color=0xaa66ea
        )
        await ctx.reply(embed=embed)


@client.command(brief='DM your message to the mentioned user')
async def dm(ctx, member: discord.Member, *, content):

    try:
        channel = await member.create_dm()
        embed = discord.Embed(title= f"{ctx.author.name}'s message",description= f"{content}", color=0xaa66ea)
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
        embed = discord.Embed(title=f"Results for **{query}**", description="Riya is **Siddhartha's** fourth child & a spammer.", color=0xFF0000)
        await ctx.reply(embed=embed)
    elif query == "Vanshika Pawar":
        embed = discord.Embed(title=f"Results for **{query}**", description="Vanshika Pawar is **Siddhartha's** first child & a terrorist.", color=0xFF0000)
        await ctx.reply(embed=embed)
    elif query == "Akshat Singh":
        embed = discord.Embed(title=f"Results for **{query}**", description="Akshat Singh is **Siddhartha's** second child and a Scammer.", color=0xFF0000)
        await ctx.reply(embed=embed)
    elif query == "Shreeya":
        embed = discord.Embed(title=f"Results for **{query}**", description="Shreeya is **Siddhartha's** Third child and a Sasti memer.", color=0xFF0000)
        await ctx.reply(embed=embed)
    elif query == "Nitesh":
        embed = discord.Embed(title=f"Results for **{query}**", description="Nitesh is **Siddhartha's** Fifth child and a 5 samosa at a time khane wala.", color=0xFF0000)
        await ctx.reply(embed=embed)
    elif query == "Raktima":
        await ctx.reply("https://tenor.com/view/chup-bilkulchup-takla-roadies-gif-20110495")
        await ctx.reply("https://tenor.com/view/hate-seriously-spoiled-the-mood-sara-mood-kharab-kar-diya-gif-17364046")
    else:
        try:
            m = await ctx.reply(f"Collecting data from servers about `{query}` ")
            results = wikipedia.summary(query, sentences = 2)
            embed = discord.Embed(title=f"Results for **{query}**", description=f"{results}", color=0xaa66ea)
            await m.delete()
            await ctx.reply(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="**Something went wrong**", description=f"{e}", color=0xaa66ea)
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
        
@client.command(brief='Changes bot status to dnd')
async def dnd(ctx):
    if client.Superuser:
        await client.change_presence(status=discord.Status.dnd)
        await ctx.reply("Trinity Status: DND")
    else:
        embed=discord.Embed(title="Use Superuser to execute this command.", color=0xaa66ea)
        await ctx.reply(embed=embed)

@client.command(brief='Changes bot status to idle')
async def idle(ctx):
    if client.Superuser:
        await client.change_presence(status=discord.Status.idle)
        await ctx.reply("Trinity Status: Idle")
    else:
        embed=discord.Embed(title="Use Superuser to execute this command.", color=0xaa66ea)
        await ctx.reply(embed=embed)

@client.command(brief='Changes bot status')
async def online(ctx):
    if client.Superuser:
        await client.change_presence(status=discord.Status.online)
        await ctx.reply("Trinity Status: Online")
    else:
        embed=discord.Embed(title="Use Superuser to execute this command.", color=0xaa66ea)
        await ctx.reply(embed=embed)



# ------------------------------------------------------------------snipe and esnipe commands---------------------------------------------------
message_edited = {}
message_deleted = {}

@client.event
async def on_message_delete(message):
    if not message.author.bot:
        if message.guild.id not in message_deleted:
            message_deleted[message.guild.id] = []
        message_deleted_list = message_deleted[message.guild.id]
        message_deleted_list = [(message, datetime.datetime.utcnow(),  message.attachments[0].url if message.attachments != [] else None)
                                ] + message_deleted_list
        message_deleted_list.pop() if len(message_deleted) >= 6 else message_deleted_list
        message_deleted[message.guild.id] = message_deleted_list


@client.command(name='snipe')
async def snipe(ctx, number: int = 1):
    if ctx.guild.id not in message_deleted:
        message_deleted[ctx.guild.id] = []
    if not 0 <= number < 6:
        await ctx.reply("Messages can be snipped in range 1, 6")
    else:
        if len(message_deleted[ctx.guild.id]) >= number:
            # slicing to get the indexed message
            message, timestp, attachment = message_deleted[ctx.guild.id][number-1]

            # Embeds  title
            embed = discord.Embed(
                color=16718362)
            messageCont = re.sub("\`", "", message.content)
            # Embed Message
            embed.add_field(name='Snipe Message: ',
                            value=f'{ messageCont[0:1000] if len(messageCont) != 0 else "Invalid format"}' if attachment is None else f'{messageCont}\u200b',
                            inline=False)
            embed.set_author(
                name=f"{message.author.display_name} ({message.author})", icon_url=message.author.avatar_url)
            # Embed footer to display about author
            embed.set_footer(
                text=f"Deleted in #{message.channel.name}",
                icon_url=str(message.guild.icon_url))
            if attachment is not None:
                embed.set_image(url=attachment)
            # Embed timestamp to get the time stamp of the deleted message
            embed.timestamp = timestp
            await ctx.send(embed=embed)

        else:
            await ctx.reply("Messages haven't been logged till there")


@client.event
async def on_message_edit(message_before, message_after):
    if not message_before.author.bot:
        if message_before.content != message_after.content:
            if message_before.guild.id not in message_edited:
                message_edited[message_before.guild.id] = []
            message_edited_list = message_edited[message_before.guild.id]
            message_edited_list = [
                (message_before, message_after, datetime.datetime.utcnow())] + message_edited_list
            message_edited_list.pop() if len(message_edited_list) >= 6 else message_edited_list
            message_edited[message_before.guild.id] = message_edited_list


@client.command(name='esnipe')
async def esnipe(ctx, index: int = 1, *_):
    if not 0 < index < 6:
        await ctx.reply("Message can be esniped in range of (1,6)")
    else:
        if ctx.guild.id not in message_edited:
            message_edited[ctx.guild.id] = []
        if len(message_edited[ctx.guild.id]) >= index:
            message_before, message_after, timestp = message_edited[ctx.guild.id][index-1]

            embed = discord.Embed(color=16718362)

            embed.add_field(name="Original Message:",
                            value=message_before.content[0:1000],
                            inline=False)

            embed.add_field(name="Edited Message:",
                            value=message_after.content[0:1000],
                            inline=False)
            embed.add_field(name='Message url:',
                            value=f'[Jump to message]({message_after.jump_url})')
            embed.timestamp = timestp

            embed.set_footer(
                text=f"Edited in #{message_before.channel.name}",
                icon_url=str(ctx.guild.icon_url))
            embed.set_author(
                name=f"{message_before.author.display_name} ({message_before.author})", icon_url=message_before.author.avatar_url)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Messages haven't been logged till there")


# tasks to clean up dicts
@tasks.loop(seconds=3600)
async def cleanup():
    print("Cleanup Initiated")
    for i in message_edited:
        edit_list = message_edited[i]
        edit_list.pop() if len(edit_list) > 1 else edit_list
        message_edited[i] = edit_list
    for i in message_deleted:
        delete_list = message_deleted[i]
        delete_list.pop() if len(delete_list) > 1 else delete_list
        message_edited[i] = delete_list



#---------------------------------------------start of help command-------------------------------------------------

help_commands: Dict = {
    'add': 'Add two numbers',
    'admin': 'Make anyone a Superuser',
    'autoreply': 'Initiate auto reply to messages',
    'bal': 'Shows you current balance',
    'clear': 'Clear messages',
    'copy': "Copy message",
    'cr': 'sets custom reply',
    'divide': 'Divide two numbers',
    'dm': 'DM your message to the mentioned user',
    'dnd': 'changes bot status to dnd',
    'esnipe': 'Edit snipe the message',
    'getinv': 'creates invite',
    'id': 'show id of mentioned user',
    'idle': 'changes bot status to idle',
    'ignore': 'ignore users from auto replies',
    'info': 'Givies information about query',
    'listening': 'Listen to the text',
    'logs': 'Changes the Guild id',
    'multiply': 'Multiply two numbers',
    'online': 'Changes bot status to online',
    'override': 'Gives you full access to the system',
    'paste': 'paste the copies message',
    'ping': 'Show bot response time',
    'playing': 'Undefined',
    "prefix": 'for changing the prefix',
    'register': 'Register yourself to Trinity Economy commands',
    'remove': 'removes user form target mode',
    'replysetup': 'initiate reply',
    'resend': 'resends the message you replied for',
    'role': 'Initiate role to a user',
    'say': 'will say your message',
    'snipe': 'Snipe deleted message',
    'stream': 'stream anything',
    'sub': 'subtract two numbers',
    'superchannel': 'for creating millions of channels',
    'targetmode': 'toggles targetmode',
    'targetusr': "targets the user",
    'te': 'Changes target emoji',
    'toggle': 'Enable/Disable commands',
    'updatebal': 'update your balance to as much you want',
    'watching': 'watch anything'
}
client.remove_command('help')

@client.command(name='help')
async def help(ctx, *args):

    embed = discord.Embed(title=f'Commands',
                          color=16718362)
    a = 1
    for command_name, command_info in help_commands.items():
        embed.add_field(name=f"{a}. {command_name}",
                        value=f"```\n{command_info}\n```",
                        inline=True)
        a += 1
    embed.set_thumbnail(url=str(ctx.guild.icon_url))

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_author(name=f"Trinity Help Panel",
                     icon_url="https://images-ext-2.discordapp.net/external/DCkc86FAVzM94joKgmW2XS6PYwItlzVi9XlPu7H9Gzg/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/889368446192734209/b70c6ea0db6f22d5d78b77635d02d19f.png")

    embed.set_footer(text=f"Hello, {ctx.author.name}",
                     icon_url="https://cdn.discordapp.com/attachments/941355481589485630/949221082076938310/pinpng.com-timer-png-723861.png")

    msg = await ctx.reply(embed=embed)
    await asyncio.sleep(60)
    await msg.delete()
#----------------------------------------------------------------end of help command----------------------------------------------------------------------------

#----------------------------------------------------------------------- restart--------------------------------------------------------------------------------

@client.command(name='restart')
async def restart(ctx):
    if ctx.message.author.id in [767758266155401226, 858195823296905256, 935187857625215046]: # saurabh, sid, om
        heroku_conn = heroku3.from_key("heorku token")
        app = heroku_conn.apps()['solicitor1232']
        app.restart()
        await ctx.reply("Restarting...")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.commadn(name='eval')
async def eval(ctx, args):
    await ctx.reply(eval)

client.run('client token')
