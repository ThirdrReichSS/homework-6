from aiogram import F
from aiogram import Router, types

callback_router = Router()

@callback_router.callback_query(F.data == 'address')
async def addres(callback: types.CallbackQuery):
    await callback.message.answer(text='our adress: near by u')

