from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='our address', callback_data='address'),
         InlineKeyboardButton(text='our website', url='https://www.toptal.com/developers/gitignore/api/python')],
        [InlineKeyboardButton(text='menu', callback_data='menu'),
         InlineKeyboardButton(text='write a feedback', callback_data='comment')]
    ])
    return kb
