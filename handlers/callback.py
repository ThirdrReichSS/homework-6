from aiogram import F
from aiogram import Router, types

callback_router = Router()


@callback_router.callback_query(F.data == 'address')
async def address(callback: types.CallbackQuery):

    await callback.message.answer(text='our address: near by u')

