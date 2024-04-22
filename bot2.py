import discord
from discord.ext import commands # this for the bot to be able to work
from dotenv import load_dotenv
import os # os imorted because its needed here




load_dotenv()
token =  os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all() # this intents can be changed in release state because of dangerous actions possible


client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def hello(ctx):
    await ctx.send('Hello, world! We are bot in developoment witch will be dynamicaly changed and growning with the communtiy')

@client.command()
async def new_client(ctx):
    await ctx.send('The website is not build at the moment ')


@client.command()
async def new_driver(ctx):
    await ctx.send ('**To register as  driver you need to pass our driver verify process!!!**')


@client.command()
async def new_server_mc(ctx):
    await ctx.send ('To have a new server message @bedrodactyl on discord he will help ya')

@client.command()
async def new_server_ets2(ctx):
    await ctx.send ('To have a new server message @bedrodactyl on discord he will help ya')



@client.command()
async def help(ctx):
    await ctx.send ('To have a new server message @bedrodacyl on discord he will help ya ')

@client.command()
async def invoice(ctx):
    await ctx.send ('if you want to be registered in our invoice system mail us at orders@hostfab.xyz ')


#client.add_command(test) ## ddeperecated

if token == None:
    print('you dont have a token in the env FILE')
client.run(token)
