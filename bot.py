from aiogram import Bot, Dispatcher
import asyncio
from handlers import user
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "8677576905:AAGlEPTyJq9419cBshZTHv2nOkID4oMUyf4"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(user)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


