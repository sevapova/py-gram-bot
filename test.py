from pygrambot.updater import Updater
from config import TOKEN


updater = Updater(TOKEN)
updater.start_polling()
