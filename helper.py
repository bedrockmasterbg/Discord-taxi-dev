from os import environ
from dotenv import load_dotenv
import discord, requests, asyncio, smtplib
from discord.ext import commands 


load_dotenv()

status_page_url = 'http://demo1.hostfab.xyz:3001/status/status'
google_maps_api_url = 'https://maps.googleapis.com/maps/api/distancematrix/json'


required_envs = [
    'DISCORD_TOKEN',
    'GOOGLE_MAPS_API_KEY',
    # 'EMAIL_ADDRESS',
   # 'EMAIL_PASSWORD'
]


for env in required_envs:
    if (not env in environ) or (len(environ[env]) == 0):
        exit(f"{env}: Missing required environment variable")


envs = {env:environ.get(env) for env in required_envs}


