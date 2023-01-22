import uuid
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import submit_markup, cancel_markup, dir_markup
from config import ADMINS
from database.bot_db import sql_command_insert

class FSMAdmin(StatesGroup):
    idm = State()
    name = State()
    dir = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.chat.id in ADMINS:
        await FSMAdmin.idm.set()
        await message.answer(f"Приветствую! ID уже получен. Продолжаем?",
                             reply_markup=cancel_markup)
    else:
        await message.answer("Вы не являетесь администратором!/"
                             "Пишите в личные сообщения!")


async def load_idm(message: types.Message, state: FSMContext):
    a = str(uuid.uuid4())
    async with state.proxy() as data:
        data['idm'] = a
        print(data)
    await FSMAdmin.next()
    await message.answer("Укажите имя ментора.")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)
    await FSMAdmin.next()
    await message.answer("Укажите направление.", reply_markup=dir_markup)


async def load_dir(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dir'] = message.text
        print(data)
    await FSMAdmin.next()
    await message.answer("Укажите возраст ментора.", reply_markup=cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) <= 0:
            await message.answer("Только положительные числа!")
        else:
            async with state.proxy() as data:
                data['age'] = message.text
                print(data)
            await FSMAdmin.next()
            await message.answer("Укажите группу", reply_markup=cancel_markup)
    except ValueError:
        await message.answer("Вводить можно только цифры!")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        print(data)
        await message.answer(f'ID: {data["idm"]}, \n'
                             f' Имя: {data["name"]}, \n'
                             f' Направление: {data["dir"]}, \n'
                             f' Возраст: {data["age"]}, \n'
                             f' Группа: {data["group"]}')
    await FSMAdmin.next()
    await message.answer("Все верно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
    elif message.text.lower() == "нет":
        await FSMAdmin.name.set()
    else:
        await message.answer('Ответ должен быть "да" или "нет".')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Cancled")

def register_handlers_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals='cancel', ignore_case=True),
                                state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_idm, state=FSMAdmin.idm)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_dir, state=FSMAdmin.dir)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
