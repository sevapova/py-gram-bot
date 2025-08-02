import time
import requests
from PyTgram_bot.message_types import Update
from PyTgram_bot.dispatcher import Dispatcher

class Updater:
    def __init__(self, token):
        self.token = token
        self.dispatcher = Dispatcher()
        self.offset = 0

    def get_updates(self):
        url = f'https://api.telegram.org/bot{self.token}/getUpdates'
        params = {'offset': self.offset}
        response = requests.get(url, params=params)
        result = response.json().get('result', [])
        
        updates = []
        for update in result:
            updates.append(Update(
                update_id=update['update_id'],
                message=update.get('message')
            ))
        return updates

    def start_polling(self):
        print("BOT ISHGA TUSHDI")
        while True:
            updates = self.get_updates()
            for update in updates:
                self.offset = update.update_id + 1
                self.dispatcher.process_update(update)
            time.sleep(1)
