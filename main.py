from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.user import user_router
from handlers.callback_menu import callback_router
from handlers.callback_kavkaz import callback_kavkaz_router

from dotenv import find_dotenv, load_dotenv

import asyncio
import os


load_dotenv(find_dotenv())


ALLOWED_UPDATES = ['message,' 'edited_message' ]


bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()




dp.include_router(user_router)
dp.include_router(callback_router)
dp.include_router(callback_kavkaz_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())