from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Стоимость"),
         KeyboardButton(text="О нас")
         ]
    ], resize_keyboard=True
)
catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Продукт 1", callback_data="one")],
        [InlineKeyboardButton(text="Продукт 2", callback_data="two")],
        [InlineKeyboardButton(text="Продукт 3", callback_data="three")],
        [InlineKeyboardButton(text="Продукт 4", callback_data="four")],
        [InlineKeyboardButton(text="Другое", callback_data="others")]
    ]
)
buy1_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее", callback_data="with_photo1")]
    ]
)
buy2_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее", callback_data="with_photo2")]
    ]
)
buy3_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее", callback_data="with_photo3")]
    ]
)
buy4_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее", callback_data="with_photo4")]
    ]
)

calories_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Рассчитать", callback_data="calories")],
        [InlineKeyboardButton(text="Формула", callback_data="formula")]
    ]
)