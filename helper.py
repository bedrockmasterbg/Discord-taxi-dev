from os import environ
from dotenv import load_dotenv


load_dotenv()


google_maps_api_url = 'https://maps.googleapis.com/maps/api/distancematrix/json'


required_envs = [
    'DISCORD_TOKEN',
    'GOOGLE_MAPS_API_KEY'
]


for env in required_envs:
    if not env in environ:
        exit(f"{env}: Missing required environment variable")


envs = {
    env:environ.get(env) for env in [
        'DISCORD_TOKEN', 'GOOGLE_MAPS_API_KEY'
    ]
}
