import time
import requests


class Updater:

    def __init__(self, token):
        self.token = token
        self.offset = 0

    def start_polling(self):
        
        while True:
            
            payload = {
                'offset': self.offset
            }
            url = f'https://api.telegram.org/bot{self.token}/getUpdates'
            r = requests.get(url=url, params=payload)

            updates = r.json()['result']

            for row_update in updates:
                self.offset = row_update['update_id'] + 1

                print(row_update['update_id'])

            time.sleep(1)
