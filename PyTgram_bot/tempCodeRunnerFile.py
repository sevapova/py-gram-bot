import time
import requests


class Updater:

    def __init__(self, token):
        self.token = token
        self.offset = 0

    def start_polling(self):
        while True:
            params = {
                'offset': self.offset
            }

            url = f'https://api.telegram.org/bot{self.token}/getUpdates'
            r = requests.get(url=url, params=params)

            updates = r.json().get('result', [])

            for update in updates:
                self.offset = update['update_id'] + 1
                print(update['update_id'])

            time.sleep(1)
