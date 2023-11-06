import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher


t = open("token.txt", "r")
token = t.readline()
bot = Bot(f"{token}")
dp = Dispatcher()

async def main():
    from handlers import dp   
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot Stoped!")
        