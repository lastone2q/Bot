from main import dp, bot
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.filters import CommandStart , Command
from aiogram.enums import ParseMode
from aiogram import types , F 
from aiogram.types import FSInputFile
import inline
from config import labs as labs_converter , price_list, monobank_link, payment_channel_id
from session_service import SessionService as SS
import requests
import json 
import yaml

@dp.message(Command("start"))
async def start(message: types.Message):
    
    telegram_id = message.from_user.id
    url = "https://api-service-tatkmdbnbq-ey.a.run.app/register"
    payload = {
        'telegram_id': telegram_id,
        "username": message.from_user.full_name
    }
    response = requests.post(url, params=payload)
    print("Response Status Code:", response.status_code)
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
     
@dp.callback_query(F.data == 'payment_step_1' ) 
async def payment_step_1(call):
    config = SS(call.from_user.id)
    telegram_id = call.from_user.id
    url = "https://api-service-tatkmdbnbq-ey.a.run.app/create_transaction_id"
    file = f"{labs_converter[config.sub]}_lab_{config.lab}_variant_{config.variant[-1]}"
    price = price_list[config.sub]
    payload = {
            'telegram_id': telegram_id,
            "order": '{"item":"'+file+'"}',
            "price": price,
        }
    response = requests.post(url, params=payload)
    data=   response.content.decode()
     
    transaction_id = json.loads(data)['Transacrion ID']
    await call.message.delete()
    await call.message.answer(f"Цe твій унікальний код транзакції. Тобі потрібно буде прикріпити його у коментарі до оплати.\n ```{transaction_id}```", 
                             parse_mode =  ParseMode.MARKDOWN,
                             reply_markup = inline.payment_step_2().as_markup()
                             )

@dp.callback_query(F.data == 'payment_step_2')
async def send_monobank_link(call):
    config = SS(call.from_user.id)
    price = price_list[config.sub]
    await call.message.answer(f"До оплати <b>{price}</b> грн.\n Ось посилання до оплати: {monobank_link} \n Не забудь прикріпити код у коментар до оплати",
                              parse_mode = ParseMode.HTML )

@dp.channel_post()
async def echo(message: types.Message):
    if message.chat.id == payment_channel_id:
        print(message.text)
        data = yaml.safe_load(message.text)
        status = data['status']
        items = data['file_names']
        user_id = data['telegram_id']
        filename = json.loads(items)['item']
        
        if status == 'Approved':
            await bot.send_message(chat_id=user_id,text=f'We have your laba its {filename}')
        if status == 'Decline':
            await bot.send_message(chat_id=user_id,text='We dont have your laba')