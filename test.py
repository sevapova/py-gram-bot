import requests
from PyTgram_bot.updater import Updater
from PyTgram_bot.handler import MessageHandler
from PyTgram_bot.message_types import Update
from config import TOKEN

def handle_message(update: Update):
    chat_id = update.message['from']['id']
    text = update.message['text']
    print(update.update_id)

    p = {
        'chat_id': chat_id,
        'text': f"Siz yubordingiz: {text}"
    }

    requests.get(
        url=f'https://api.telegram.org/bot{TOKEN}/sendMessage',
        params=p
    )

updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(handle_message))
updater.start_polling()
