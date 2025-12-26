import discord
import os
from os.path import join, dirname
import random
from GoogleNews import GoogleNews
from discord.ext import commands,tasks
from asyncio import sleep as ss
#from dotenv import load_dotenv
#from dotenv import load_dotenv,find_dotenv
#from alive import keep_alive
import wolframalpha
import requests,json,random
#load_dotenv()
token=os.environ.get('DISCORD_TOKEN')
api=os.environ.get('api')
gapi=os.environ.get('google_news_api')
url=os.environ.get('emoji_api')
espression_emoji=['face-with-raised-eyebrow','thinking-face','face-with-rolling-eyes','sleeping-face','exploding-head','face-with-monocle','flushed-face']
intents = discord.Intents.default()
intents.message_content = True
client=commands.Bot(command_prefix='!',intents=intents)
#client=commands.Bot(command_prefix='!')
gapi=os.environ.get('google_news_api')
#client = discord.Client()

frd=['hey tail','you fradu','bad boy','nithin','hey you get lost']
greetings=['hello','hi','hola','hey',"what's up"]
greetings_response=["Hello!", "Good to see you again!", "Hi there, how can I help?","It's great seeing you. I hope you're doing well."]
start="Hello there I'm back"
maintan='Bot is under maintanence,do not disturb'
image='https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.toiimg.com%2Fphoto%2Fmsid-73324354%2F73324354.jpg%3F163266&imgrefurl=https%3A%2F%2Ftimesofindia.indiatimes.com%2Fentertainment%2Ftamil%2Fmovies%2Fbox-office%2Fvijays-master-pre-release-business-touches-rs-200-crore%2Farticleshow%2F73324354.cms&tbnid=rAJC6Rt_Slm-zM&vet=12ahUKEwiK6Kra8JbwAhWDhUsFHRdVC8kQMygAegUIARDIAQ..i&docid=56UTIOK0GlYNZM&w=1200&h=900&q=master%20image&ved=2ahUKEwiK6Kra8JbwAhWDhUsFHRdVC8kQMygAegUIARDIAQ'
wolf=wolframalpha.Client(api)

@client.event
async def on_ready():
    #print('Iam back {0.user}'.format(client))
    #print(client.guilds[0])
    await client.change_presence(status=discord.Status.online,activity=discord.Game('under maintanence'))
    await client.get_channel(828681874057854989).send(start)
    
    try:
        await client.user.edit(password=None, avatar=image)
    except Exception:
        pass
    """for guild in client.guilds:
        print(guild)"""
    
       
@client.command(aliases=greetings)
async def _hello(ctx):
    s='<@!'+str(ctx.author.id)+'>'
    """print(ctx.author)
    print(ctx.message)
    print(ctx.guild)"""
    await ctx.send(random.choice(greetings_response)+" "+s)
@client.command(name='lol')
async def _lol(ctx):
    req=requests.get(url.format('rolling-on-the-floor-laughing'))
    emoj=req.json()
    await ctx.send(emoj[0]['character']*random.randint(0,5))

@client.command(aliases=['goodbye','bye','Bye','Goodbye', "see you later", "gotta go", "i have to go", "see you"])     
async def _bye(ctx):
    await ctx.send(random.choice(["bye", "talk to you later"])+'\N{THUMBS UP SIGN}')

@client.command()
async def remainder(ctx,time:int,*,msg):
    while True:
        await ss(time)
        await ctx.send(f'{msg}, {ctx.author.mention}')
@client.command()
async def cal(ctx,*,arg):
    res=wolf.query(arg)    
    await ctx.send(next(res.results).text)

@client.command()
async def clear(ctx,amt:int):
    try:
        await ctx.channel.purge(limit=amt)
    except Exception:
        pass
@client.command()
async def myinfo(ctx):

   # print(ctx.author,ctx.author.id,ctx.guild.name,ctx.guild.description)
    #print(ctx.guild.id,ctx.guild.owner)
    #name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    name=str(ctx.author)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)
    status=ctx.author.status
    embed = discord.Embed(
        title=name + "  Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name='ID',value=ctx.author.id,inline=False)
    embed.add_field(name="Name", value=name, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name='Status',value=status,inline=True)

    await ctx.send(embed=embed)

@client.command()
async def news(ctx):
    res=requests.get(gapi)
    res=res.json()
    for i in res['articles']:
        if i['author']==None:
            author='updates'
        else:
            author=i['author']
        embed = discord.Embed(
        title=i['title'] ,
        description="*"+author+"*",
        color=discord.Color.purple())
        embed.set_thumbnail(url=i['urlToImage'])
        embed.add_field(name='Description',value="`"+i['description']+"`",inline=False)
        await ctx.send(embed=embed)
        
@client.command()
async def gnews(ctx,*,txt):
    google=GoogleNews('en')
    google.search(txt)
   # print(txt)
    for i in google.result():
        await ctx.send(i['title'])

@client.event
async def on_member_join(member):
    for chnl in member.server.channels:
        if str(chnl)=='announcements':
            await client.get_channel(828681874057854989).send(f"welcome to the fraud server{member.mention}")

@client.event
async def on_error(event, *args, **kwargs):
    #message = args[0]
   # print(event)
    emoj=requests.get(url.format(random.choice(espression_emoji))).json()
    await client.get_channel(828681874057854989).send(emoj[0]['character'])
@client.event
async def on_command_error(ctx,error):
    emoj=requests.get(url.format(random.choice(espression_emoji))).json()
    await ctx.get_channel(828681874057854989).send(emoj[0]['character'])    

#keep_alive()
client.run(token)
