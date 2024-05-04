from aiogram.filters import Command
from aiogram import Router, types
from aiogram.types import FSInputFile
import os
from random import choice


pic_router = Router()

@pic_router.message(Command('picture'))
async def picture(message: types.Message):
    path = 'media/Unknown.jpeg'
    file = FSInputFile(path)
    await message.answer_photo(photo=file, caption='beautiful picture')


@pic_router.message(Command('picture_random'))
async def picture_random(message: types.Message):
    photos = os.listdir('media/')
    path = f'media/{choice(photos)}'
    print(photos)
    file = FSInputFile(path)
    await message.answer_photo(photo=file, caption='beautiful picture')