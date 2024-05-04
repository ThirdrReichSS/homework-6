from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def menu_kb():
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='first meal'),
         KeyboardButton(text='dinner'),
         KeyboardButton(text='dinner')],
        [KeyboardButton(text='tea'),
         KeyboardButton(text='coke'),
         KeyboardButton(text='pepsi')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True)
    return kb

