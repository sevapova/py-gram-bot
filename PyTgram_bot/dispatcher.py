from PyTgram_bot.message_types import Update

class Dispatcher:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def process_update(self, update: Update):
        for handler in self.handlers:
            if handler.check_update(update):
                handler.callback(update)
