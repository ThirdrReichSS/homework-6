from aiogram import Router, F, types
# from aiogram. filters import Command
from aiogram. fsm. state import State, StatesGroup
from aiogram. fsm.context import FSMContext
# from bot import db


comment_router = Router()


# FSM - Finite State Machine - конечный автомат
class Comments(StatesGroup):
    name = State()
    contacts = State()
    date = State()
    quality_of_our_foods = State()
    clean = State()
    additional_comment = State()


# - как вас зовут
# - ваш номер телефона или ваш инстаграмм
# - дата вашего посещения нашего заведения тут можно сделать проверку чтоб оыли только цифры
# - как оцениваете качество еды (текстовая клавиатура со значениями - плохо, удовлетворительно и тдз)
# - как оцениваете чистоту заведения
# - Дополнительные комментарии(тут пользователь может ввести много текста)

@comment_router.callback_query(F.data == 'comment')
async def start_comment(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('your name: ')
    await state.set_state(Comments.name)


@comment_router.message(Comments.name)
async def load_name(message: types.Message, state: FSMContext):
    await message.answer('write your phone number or instagram: ')
    await state.set_state(Comments.contacts)


@comment_router.message(Comments.contacts)
async def load_contacts(message: types.Message, state: FSMContext):
    await message.answer('when did u visit our cafe')
    await state.set_state(Comments.date)

@comment_router.message(Comments.date)
async def load_date(message: types.Message, state: FSMContext):
    await message.answer(' rate our foods from 1 to 10')
    await state.set_state(Comments.quality_of_our_foods)


@comment_router.message(Comments.quality_of_our_foods)
async def load_quality(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('write only the number')
    elif not 1 <= int(message.text) <= 10:
        await message.answer('write the mark from 1 to 10')
    else:
        await message.answer('rent the pure of our cafe')
    await state.set_state(Comments.clean)


@comment_router.message(Comments.clean)
async def load_clean(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('write only the number')
    elif not 1 <= int(message.text) <= 10:
        await message.answer('write the mark from 1 to 10')
    else:
        await message.answer('write ur opinion about of cafe')
    await state.set_state(Comments.additional_comment)


@comment_router.message(Comments.additional_comment)
async def load_additional_comment(message: types.Message, state: FSMContext):
    await message.answer('thanks for ur opinion\n'
                         'have a nice day')
    await state.clear()
    # await state.set_state(Comments.date)



