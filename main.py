import discord, requests
from discord.ext import commands
from fees import *
from helper import *


class Taxi_Bot:
    def __init__(self):
        self.intents = discord.Intents.all()
        self.client = commands.Bot(
            command_prefix='!',
            intents=self.intents
        )

        self.functions()


    def get_google_maps_params(self, pickup, dropoff):
        return {
            'origins': pickup,
            'destinations': dropoff,
            'key': envs['GOOGLE_MAPS_API_KEY']
        }
    

    def get_taxi_price(self, distance):
        fare = distance * fare_rate

        return fare + idle_fee + service_fee + call_fee


    def functions(self):
        @self.client.event
        async def on_ready():
            print('Bot is ready')


        @self.client.command()
        async def simeon(ctx):
            await ctx.send('Doveri mi se')


        @self.client.command()
        async def hello(ctx):
            await ctx.send('Hello! this bot is for a taxi service. You can use the following commands: \n')


        @self.client.command()
        async def ping(ctx):
            await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')


        @self.client.command()
        @commands.has_any_role('Admin', 'Moderator', 'Server Supporter')
        async def register_client(ctx):
            def check(m):
                return (m.author == ctx.author) and (m.channel == ctx.channel)

            await ctx.send("Please provide your name, email and phone number")
            msg = await self.client.wait_for('message', check=check)

            owner = ctx.guild.owner
            await owner.send(f"New client registration:\n{msg.content}")


        @self.client.command()
        async def register_driver(ctx):
            def check(m):
                return (m.author == ctx.author) and (m.channel == ctx.channel)

            await ctx.send("Please provide your name, phone number, and email address")
            msg = await self.client.wait_for('message', check=check)

            owner = ctx.guild.owner
            await owner.send(f"New driver registration:\n{msg.content}")


        @self.client.command()
        @commands.has_any_role('Admin', 'Moderator', 'Server Supporter')
        async def register_vehicle(ctx):
            def check(m):
                return (m.author == ctx.author) and (m.channel == ctx.channel)

            await ctx.send("Please provide your vehicle type, plate number, and color")
            owner = ctx.guild.owner

            msg = await self.client.wait_for('message', check=check)
            await owner.send(f"New vehicle registration:\n{msg.content}")


        @self.client.command()
        async def price(ctx, distance=None):
            try:
                total = self.get_taxi_price(distance)
                await ctx.send(f'The total price for the trip is ${total:.2f}')

            except:
                await ctx.send(f'**{distance}** is not a valid unit\nSyntax: !price **<distance>** (in km)')


        @self.client.command()
        @commands.has_any_role('Owner', 'Admin', 'Moderator','Server Supporter')
        async def new_order(ctx):
            def check(m):
                return (m.author == ctx.author) and (m.channel == ctx.channel)

            await ctx.send("Please provide your pickup location")
            pickup_msg = await self.client.wait_for('message', check=check)

            await ctx.send("Please provide your dropoff location")
            dropoff_msg = await self.client.wait_for('message', check=check)

            params = self.get_google_maps_params(pickup_msg.content, dropoff_msg.content)
            response = requests.get(google_maps_api_url, params=params)
            response_json = response.json()

            print(response.text)

            try:
                pickup_address = response_json['origin_addresses'][0]
                dropoff_address = response_json['destination_addresses'][0]

                if len(pickup_address) == 0:
                    await ctx.send('**Pickup address** not found!')
                    return True

                elif len(dropoff_address) ==  0:
                    await ctx.send('**Dropoff address** not found!')
                    return True

                distance = response_json['rows'][0]['elements'][0]['distance']['value'] / 1000
                duration = response_json['rows'][0]['elements'][0]['duration']['text']
                total = self.get_taxi_price(distance)

                success_msg = f'''**Order placed**

Pickup from: **{pickup_address}**
Dropoff at: **{dropoff_address}**

Distance: **{distance:.2f}** km
Estimated travel duration: **{duration}**

Total price: **${total:.2f}**
'''

                await ctx.send(success_msg)

            except:
                fail_msg = f'''**Order failed**
Could not process your taxi order with the requested addresses. Try again with more precise locations.
'''

                await ctx.send(fail_msg)


bot = Taxi_Bot()
bot.client.run(token=envs['DISCORD_TOKEN'])
