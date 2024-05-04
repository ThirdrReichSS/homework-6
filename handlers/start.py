from aiogram.filters import Command
from aiogram import Router, types
from keyboards.start_kb import start_kb
start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    text = f'Hello {message.from_user.full_name} '
    await message.answer(text, reply_markup=start_kb())


@start_router .message(Command('info'))
async def info(message: types.Message):
    text = (f'Your id is {message.from_user.id}\n'
            f'Your username is {message.from_user.username}\n'
            f'Your fullname is {message.from_user.full_name}\n')
    await message.answer(text=text)
