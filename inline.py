from aiogram.utils.keyboard import InlineKeyboardBuilder 
import content


class faculty:
    builder = InlineKeyboardBuilder()
    for i in content.faculty():
        builder.button(text= i, callback_data= i)
    builder.adjust(1)

#def subjects():
    #builder_subjects = InlineKeyboardBuilder()
    #builder_subjects.button(text= )

class labs:
    builder = InlineKeyboardBuilder()

