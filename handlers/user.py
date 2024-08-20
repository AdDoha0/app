from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram import Router


user_router = Router()


@user_router.message(CommandStart())
async def start_command(message: Message) -> None:
    start_message = """
Приветствую! 👋 Добро пожаловать, этот бот станет вашим проводником по удивительным местам Кавказа! 🌄

Кавказ – это уникальный регион, где пересекаются культуры и традиции, а природа поражает своим разнообразием и величием. Здесь вас ждут:

- 🏔 Величественные горы и живописные ущелья.
- 🏞 Удивительные природные парки, где можно насладиться тишиной и красотой первозданной природы.
- 🕌 Богатая история и культура народов Кавказа, отразившаяся в архитектуре, музыке и традициях.
- 🍽 Неповторимая кухня, в которой сочетаются разнообразные вкусы и ароматы.

С нашим ботом вы сможете:

- 📍 Найти лучшие маршруты и достопримечательности, которые стоит посетить.
- 📅 Спланировать свое путешествие так, чтобы оно стало незабываемым и комфортным.

Начните свое кавказское приключение с нами и погрузитесь в атмосферу этого удивительного края! Если у вас возникнут вопросы или нужны советы, просто введите команду, и мы всегда будем рядом. Удачного путешествия! 🚀
"""


    kb_start = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать путешествие ✅ ", callback_data="start")]
    ])

    await message.answer(start_message, reply_markup=kb_start)




@user_router.callback_query(lambda callback: callback.data == "start")
@user_router.message(Command('menu'))
async def menu(callback: CallbackQuery) -> None:
    kb_inline = InlineKeyboardMarkup(inline_keyboard=
        [
            [InlineKeyboardButton(text="Водитель 🧳", callback_data="profile_driver")],
            [InlineKeyboardButton(text="Машина 🚙", callback_data="car_info")],
            [InlineKeyboardButton(text="Что вам может показать кавказ? 🗺️", callback_data="kavkaz_info")],
            [InlineKeyboardButton(text="Отзывы 🔥", url="https://t.me/chechturizm")],
            [InlineKeyboardButton(text="Наша группа 🔥", url="https://t.me/Turkavkaz9505")]
        ]
    )

    await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id= callback.message.message_id)
    await callback.message.answer("Выберите интересующий вас пункт меню", reply_markup=kb_inline)