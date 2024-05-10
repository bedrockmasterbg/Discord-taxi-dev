import discord
import os
from discord.ext import commands
from  dotenv import load_dotenv
import aiohttp, math, time

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
google_maps_key = os.getenv('google_maps_api_key')
intents = discord.Intents.all() # used for development only
#intents = discord.Intents.defalt() # will be used in production
#intents.messages = True # will be used in production
client = commands.Bot(command_prefix='!', intents=intents)
idle_fee = 0.39  # Define your idle fee here
service_fee = 0.139  # Define your service fee here
call_fee = 1.0  # Define your call fee here

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def simeon(ctx):
    await ctx.send('Doveri mi se')


@client.command()
async def hello(ctx):
    await ctx.send('Hello! this bot is for a taxi service. You can use the following commands: \n')
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
@client.command()
async def price(ctx, distance: float):
    fare_rate = 0.83  # Define your fare rate here
    idle_fee = 0.39  # Define your idle fee here
    service_fee = 0.139  # Define your service fee here
    call_fee = 1.0  # Define your call fee here
    fare = distance * fare_rate
    total = fare + idle_fee + service_fee + call_fee
    await ctx.send(f'The total price for the trip is ${total:.2f}')





@client.command()
@commands.has_any_role('Admin', 'Moderator', 'Server Supporter')
async def register_client(ctx):

    await ctx.send("Please provide your name, email and phone number")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    msg = await client.wait_for('message', check=check)

    owner = ctx.guild.owner
    await owner.send(f"New client registration:\n{msg.content}")


@client.command()
async def register_driver(ctx):
    await ctx.send("Please provide your name, phone number, and email address")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    msg = await client.wait_for('message', check=check)

    owner = ctx.guild.owner
    await owner.send(f"New driver registration:\n{msg.content}")

@client.command()
@commands.has_any_role('Admin', 'Moderator', 'Server Supporter')
async def register_vehicle(ctx):
    await ctx.send("Please provide your vehicle type, plate number, and color")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    owner = ctx.guild.owner
    msg = await client.wait_for('message', check=check)
    await owner.send(f"New vehicle registration:\n{msg.content}")


@client.command()
async def наргиле(ctx):
    await ctx.send("Аре флейм брат!")

@client.command()
async def blocking(ctx):
    await ctx.send("блокинга си е в действието")
@commands.has_any_role('Admin', 'Moderator', 'Server Supporter')
async def shefkata(ctx):
    await ctx.send("Вързан без крака аха")

@client.command()
@commands.cooldown(1, 6, commands.BucketType.user) # this cooldown is used for not allowing users to spam google maps api 
@commands.has_any_role('Admin', 'Moderator',) #this 
async def new_order(ctx):
    await ctx.send("Please provide your pickup location")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    pickup_msg = await client.wait_for('message', check=check)

    await ctx.send("Please provide your dropoff location")
    dropoff_msg = await client.wait_for('message', check=check)

    # Calculate distance between pickup and dropoff locations
    async with aiohttp.ClientSession() as session:
        params = {
            'origins': pickup_msg.content,
            'destinations': dropoff_msg.content,
            'key': google_maps_key
        }
        async with session.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=params) as resp:
            data = await resp.json()
            distance = data['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convert meters to kilometers

    fare_rate = 1.49  # Define your fare rate here
    fare = distance * fare_rate
    total = fare + idle_fee + service_fee + call_fee
    await ctx.send(f'Your order has been placed. The total price for the trip is ${total:.2f} and the total distance is {distance:.2f} km')


# dev  check
if token is None:
    print("Token is missing")
else:
    print('Token is available')

client.run(token)   