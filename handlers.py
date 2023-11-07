from main import dp, bot
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.filters import CommandStart , Command
from aiogram.enums import ParseMode
from aiogram import types , F 
from aiogram.types import FSInputFile
import inline
from config import labs as labs_converter
from session_service import SessionService as SS

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привіт <b>{message.from_user.full_name}</b>, вибери свою спеціальність", parse_mode=ParseMode.HTML, reply_markup= inline.spec_inline().as_markup())
    

@dp.callback_query(F.data.endswith('_'))
async def speciality(call):
    config = SS(call.from_user.id)
    if not call.data.startswith('back'):
        config.spec = call.data[:-1]
    await call.message.edit_text("Вибери потрібний тобі предмет", parse_mode = ParseMode.HTML, reply_markup= inline.sub_inline(config.spec).as_markup())

@dp.callback_query(F.data.endswith('!'))
async def labs(call):
    config = SS(call.from_user.id)
    if not call.data.startswith('back'):
        config.sub = call.data[:-1]
    await call.message.edit_text("Вибери номер лабораторної", parse_mode = ParseMode.HTML, reply_markup= inline.labs_inline(config.spec, config.sub).as_markup())

@dp.callback_query(F.data.endswith('?'))
async def variant(call):
    config = SS(call.from_user.id)
    if not call.data.startswith('back'):
        config.lab = call.data[:-1]
    try:
        await call.message.edit_text("Вибери варіант", parse_mode = ParseMode.HTML, reply_markup= inline.variants_inline(config.spec, config.sub, config.lab).as_markup())    
    except Exception:
        await call.message.delete()
        await call.message.answer("Вибери варіант", parse_mode = ParseMode.HTML, reply_markup= inline.variants_inline(config.spec, config.sub, config.lab).as_markup())    
@dp.callback_query(F.data.endswith('+'))
async def start_back(call):
    await call.message.edit_text(f"Привіт <b>{call.from_user.full_name}</b>, вибери свою спеціальність", parse_mode=ParseMode.HTML, reply_markup= inline.spec_inline().as_markup())

@dp.callback_query(F.data.endswith('$'))
async def start_user_activity(call):
    config = SS(call.from_user.id)
    if not call.data.startswith('back'):
        config.variant = call.data[:-1]
    await call.message.edit_text(f"{config.sub}, номер лабораторної {config.lab}, {config.variant}")
        # Send the image with a caption (description)
    photo = FSInputFile(f"preview/{labs_converter[config.sub]}_lab_{config.lab}_variant_{config.variant[-1]}.png")
    caption = "Це завдання обраної лабараторної роботи. Перед покупкою рекомендуємо перевірити чи вони співпадають із твоїми."
    await call.message.answer_photo(
        photo = photo,
        caption=caption,
        reply_markup = inline.confirm_lab().as_markup()
        )      
     
    # await call.message.edit_text(caption, reply_markup = inline.confirm_lab("!").as_markup())

      
