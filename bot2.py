import discord
from pydactyl import PterodactylClient
from discord.ext import commands # this for the bot to be able to work
from dotenv import load_dotenv
import os # os imorted because its needed here
#import logging # loggin is unsed library for now 


api = PterodactylClient('debug','anything')
#Removed pterotoken and url

#DEFINING PRICES for our taxi service
fare_rate = 0.83 
idle_fee = 0.39
service_fee = 0.05
call_fee = 1.40


load_dotenv()
token =  os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()


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
     api.servers.create_server(name='PaperServerCreated by BOt', user_id=1, nest_id=4,
                          egg_id=3, memory_limit=8000, swap_limit=0,
                          backup_limit=0, disk_limit=10240, location_ids=[1])
        await ctx.send ('the server has been created')

@client.command()
async def new_server_ets2(ctx):
    api.servers.create_server(name='My Paper Server', user_id=1, nest_id=4,
                          egg_id=3, memory_limit=8000, swap_limit=0,
                          backup_limit=0, disk_limit=10240, location_ids=[1])
    await ctx.send ('Congrats you created a server')

@client.command()
async def invoice(ctx):
    await ctx.send ('if you want to be registered in our invoice system mail us at orders@hostfab.xyz ')

@client.command()
async def page_info(ctx):
    await ctx.send ('our status page is: http://testnode.hostfab.xyz:3001/status/status ')  

@client.command()
async def prices(ctx):
    await ctx.send(f'our prices are our fare rate is : {fare_rate},Idle fee is :{idle_fee},Service fee:{service_fee},Call fee is :{call_fee} please remind the driver to tell you what is the total in the end')
#client.add_command(test) ## ddeperecated




if token == None:
    print('you dont have a token in the env FILE')

client.run(token)
