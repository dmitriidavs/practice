import os

from bot import bot, dp

from aiogram import types, Dispatcher, Bot
from fastapi import FastAPI


webhook_path = f'/bot/{os.environ.get("BOT_API_TOKEN")}'
webhook_url = os.environ.get('WEBHOOK_URL') + webhook_path

app = FastAPI()


@app.on_event('startup')
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info != webhook_url:
        await bot.set_webhook(
            url=webhook_url
        )


@app.post(webhook_path)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event('shutdown')
async def on_shutdown():
    pass
