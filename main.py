import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import texts
from config import *
from texts import *
from keyboards import *
logging.basicConfig(level=logging.INFO)
API = ""
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(texts.start, reply_markup=start_kb)
@dp.message_handler(text=["О нас"])
async def about(message):
    await message.answer(texts.about, reply_markup=start_kb)
@dp.message_handler(text=["Стоимость"])
async def price(message):
    await message.answer("Что вас интересует?", reply_markup=catalog_kb)

@dp.callback_query_handler(text=["one"])
async def buy_1(call):
    await call.message.answer(texts.product1, reply_markup=buy1_kb)
    await call.answer()

@dp.callback_query_handler(text=["two"])
async def buy_2(call):
    await call.message.answer(texts.product2, reply_markup=buy2_kb)
    await call.answer()

@dp.callback_query_handler(text=["three"])
async def buy_3(call):
    await call.message.answer(texts.product3, reply_markup=buy3_kb)
    await call.answer()

@dp.callback_query_handler(text=["four"])
async def buy_4(call):
    await call.message.answer(texts.product4, reply_markup=buy4_kb)
    await call.answer()

@dp.callback_query_handler(text=["others"])
async def buy_4(call):
    await call.message.answer(texts.other, reply_markup=calories_kb)
    await call.answer()

@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст")
    await UserState.age.set()
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer("Введите свой вес")
    await UserState.weight.set()
@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    await message.answer(f"Ваша норма калорий: {float(data['third']) * 10 + 6.25 * float(data['second']) - 5 * float(data['first']) - 161}", reply_markup=calories_kb)
    await state.finish()
@dp.callback_query_handler(text="formula")
async def formula(call):
    await call.message.answer(texts.formulas)
    await call.answer()
@dp.callback_query_handler(text="with_photo1")
async def about_prod1(call):
    with open("img1.jpg", "rb") as img1:
        await call.message.answer_photo(img1, texts.about_prod1, reply_markup=catalog_kb)
        await call.answer()
@dp.callback_query_handler(text="with_photo2")
async def about_prod2(call):
    with open("img2.jpg", "rb") as img2:
        await call.message.answer_photo(img2, texts.about_prod2, reply_markup=catalog_kb)
        await call.answer()
@dp.callback_query_handler(text="with_photo3")
async def about_prod3(call):
    with open("img3.jpg", "rb") as img3:
        await call.message.answer_photo(img3, texts.about_prod3, reply_markup=catalog_kb)
        await call.answer()
@dp.callback_query_handler(text="with_photo4")
async def about_prod4(call):
    with open("img4.jpg", "rb") as img4:
        await call.message.answer_photo(img4, texts.about_prod4, reply_markup=catalog_kb)
        await call.answer()
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

