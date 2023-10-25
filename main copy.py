import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types , F
from aiogram.filters import CommandStart , Command
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder 

t = open("token.txt", "r")
token = t.readline()

dp = Dispatcher()



@dp.message(Command("start"))
async def start(message: types.Message): 
    builder = InlineKeyboardBuilder()
    builder.button(text= "КН", callback_data= "КН все ок")
    builder.button(text= "ІПЗ", callback_data= "ІПЗ")
    builder.button(text= "КБ", callback_data= "КБ")
    builder.button(text= "АКІТ", callback_data= "АКІТ")
    await message.answer(f"Привіт <b>{message.from_user.full_name}</b>, вибери свою спеціальність", parse_mode=ParseMode.HTML, reply_markup= builder.as_markup())

@dp.callback_query(F.data.startswith('КН'))
async def callback(call):
    builder_subjects = InlineKeyboardBuilder()
    builder_subjects.button(text = "ОП", callback_data= "ОП")
    builder_subjects.button(text = "Предмет 2", callback_data= "ХЗ")
    await call.message.answer("Виберіть потрібний вам предмет", parse_mode = ParseMode.HTML, reply_markup = builder_subjects.as_markup())  

async def main():   
    bot = Bot(f"{token}")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot Stoped!")
        