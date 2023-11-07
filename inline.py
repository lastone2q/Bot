from aiogram.utils.keyboard import InlineKeyboardBuilder 
import content


def spec_inline():
    builder = InlineKeyboardBuilder()
    for i in content.spec():
        builder.button(text= i, callback_data= i + '_')
    builder.adjust(2)
    return builder

def sub_inline(call_):
    builder = InlineKeyboardBuilder()
    for i in content.sub(call_):
        builder.button(text= i, callback_data= i + '!')
    back("+", builder)
    builder.adjust(1)
    return builder

def labs_inline(spec , sub):
    builder = InlineKeyboardBuilder()
    for i  in content.lab(spec, sub):
        builder.button(text= str(i), callback_data= str(i) + '?' )
    back("_" , builder)
    builder.adjust(2)
    return builder

def variants_inline(spec, sub ,lab):
    builder = InlineKeyboardBuilder()
    for i in content.var(spec, sub , lab):
        builder.button(text= i, callback_data= str(i) + '$')
    back("!" , builder)
    builder.adjust(2)
    return builder

def back(step , builder,):
    builder.button(text= "Назад" , callback_data= "back" + step)
    

def confirm_lab():
    builder = InlineKeyboardBuilder()
    meta_data = [('Продовжити покупку', 'payment_step_1') ]
    for i in meta_data:
        text = i[0]
        callback_data = i[1]
        builder.button(text=text, callback_data=callback_data) 
    back("?", builder)
    builder.adjust(1)
    return builder