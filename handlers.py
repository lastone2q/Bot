from main import dp
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.filters import CommandStart , Command
from aiogram.enums import ParseMode
from aiogram import types , F 
import inline
import config


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привіт <b>{message.from_user.full_name}</b>, вибери свою спеціальність", parse_mode=ParseMode.HTML, reply_markup= inline.spec_inline().as_markup())
    

@dp.callback_query(F.data.endswith('_'))
async def speciality(call):
    if not call.data.startswith('back'):
        config.spec = call.data[:-1]
    await call.message.edit_text("Вибери потрібний тобі предмет", parse_mode = ParseMode.HTML, reply_markup= inline.sub_inline(config.spec).as_markup())

@dp.callback_query(F.data.endswith('!'))
async def labs(call):
    if not call.data.startswith('back'):
        config.sub = call.data[:-1]
    await call.message.edit_text("Вибери номер лабораторної", parse_mode = ParseMode.HTML, reply_markup= inline.labs_inline(config.spec, config.sub).as_markup())

@dp.callback_query(F.data.endswith('?'))
async def variant(call):
    if not call.data.startswith('back'):
        config.lab = call.data[:-1]
    await call.message.edit_text("Вебери варіант", parse_mode = ParseMode.HTML, reply_markup= inline.variants_inline(config.spec, config.sub, config.lab).as_markup())    

@dp.callback_query(F.data.endswith('+'))
async def start_back(call):
    await call.message.edit_text(f"Привіт <b>{call.from_user.full_name}</b>, вибери свою спеціальність", parse_mode=ParseMode.HTML, reply_markup= inline.spec_inline().as_markup())


      
