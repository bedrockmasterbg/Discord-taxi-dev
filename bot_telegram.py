from telegram import Update # for handling updates
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext # for handling commands
import json # for handling JSON files
from dotenv import load_dotenv # for loading environment variables #
load_dotenv() # Load environment variables from .env file
TOKEN = os.getenv('telegram_bot_token') # Get the token from the .env file





def location(update: Update, context: CallbackContext) -> None:
    message = update.message
    current_location = message.location
    user_id = message.from_user.id

    # Save location to a dictionary
    location_data = {
        'user_id': user_id,
        'latitude': current_location.latitude,
        'longitude': current_location.longitude
    }

    # Append location data to a JSON file
    with open('locations.json', 'a') as f:
        json.dump(location_data, f)
        f.write('\n')

def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.location, location))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()