from PyTgram_bot.message_types import Update

class MessageHandler:
    def __init__(self, callback):
        self.callback = callback

    def check_update(self, update: Update):
        return update.message is not None
