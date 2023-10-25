from main import dp
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.filters import CommandStart , Command
from aiogram.enums import ParseMode
from aiogram import types , F
import inline
import content

@dp.message(Command("start"))
async def start(message: types.Message): 
    await message.answer(f"Привіт <b>{message.from_user.full_name}</b>, вибери свою спеціальність", parse_mode=ParseMode.HTML, reply_markup= inline.faculty.builder.as_markup())

@dp.callback_query()
async def faculty(call):
    sub = []
    for i in content.faculty():
        if call.data == i:
            builder = InlineKeyboardBuilder()
            for y in content.subjects(i):
                y = y.strip()
                sub.append(y)
                builder.button(text= y, callback_data= y)
                builder.adjust(1)
            await call.message.edit_text("Виберіть потрібний вам предмет", parse_mode = ParseMode.HTML, reply_markup = builder.as_markup())
    #for i in sub:
        #if call.data ==  i:

            