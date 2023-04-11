import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher


bot = Bot(token=os.environ.get('BOT_API_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Hello, {message.from_user.first_name}')
