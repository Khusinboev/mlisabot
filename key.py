from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()


TOKEN = "1957686323:AAFTO9qyaRWb9VKJ0HOyfRqjEZqbRcg4hFo"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot, storage=storage)
