import asyncio
import logging
import sys
from aiogram import Router
from aiogram import Bot, Dispatcher
 
from config import TUNNEL_URL
from aiogram import types
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

t = open("token.txt", "r")
token = t.readline()
 
WEBHOOK_PATH = f"/bot/{token}"
WEBHOOK_URL = f"{TUNNEL_URL}{WEBHOOK_PATH}"


bot = Bot(f"{token}")
dp = Router()



# async def main():
#     from handlers import dp   
#     await dp.start_polling(bot)
    
# @app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
     

    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )
    
def main() -> None:
    # Dispatcher is a root router
    from handlers import dp
    dispatcher = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dispatcher.include_router(dp)

    # Register startup hook to initialize webhook
    dispatcher.startup.register(on_startup)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(token, parse_mode=ParseMode.HTML)

    # Create aiohttp.web.Application instance
    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dispatcher,
        bot=bot,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dispatcher, bot=bot)

    # And finally start webserver
    web.run_app(app, host= "0.0.0.0", port=8000)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()