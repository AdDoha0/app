from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, FSInputFile
from aiogram import Router, F

from data.info import guide_info, car_description, why_choose_me, kavkaz_highlights
from additional_tools.utils import create_back


callback_router = Router()



@callback_router.message(Command("profile_driver"))
@callback_router.callback_query(lambda callback: callback.data == "profile_driver")
async def profile_driver(callback: CallbackQuery):
    photo_path = r"img\driver_and_car\photo_2024-01-04_14-06-32.jpg"
    photo = FSInputFile(photo_path) # загружаем фото в переменную

    kb_inline = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Почему выбирают именно меня? 🏆", callback_data="why_choose_me")],
        [InlineKeyboardButton(text="Вернутся назад 👈", callback_data="start")],
    ])


    await callback.message.bot.delete_message(chat_id=callback.message.chat.id,message_id= callback.message.message_id)
    await callback.message.answer_photo(photo=photo, caption=guide_info, reply_markup=kb_inline)




@callback_router.callback_query(lambda callback: callback.data == "why_choose_me")
async def profile_driver(callback: CallbackQuery):

    kb_inline = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Вернутся назад 👈", callback_data="profile_driver")],
        [InlineKeyboardButton(text="Вернутся в меню 👈", callback_data="start")]
    ])


    await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id= callback.message.message_id)
    await callback.message.answer(text=why_choose_me, reply_markup=kb_inline)



#--------------- DRIVER ----------------------------------------------------



@callback_router.message(Command("car_info"))
@callback_router.callback_query(lambda callback: callback.data == "car_info")
async def profile_driver(callback: CallbackQuery):
    photo_path = r"img\driver_and_car\photo_2022-11-22_21-25-45.jpg"
    photo = FSInputFile(photo_path)

    await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id= callback.message.message_id)
    await callback.message.answer_photo(photo=photo, caption=car_description, reply_markup=create_back("start"))




#--------------- CAR ----------------------------------------------------




@callback_router.message(Command("kavkaz_info"))
@callback_router.callback_query(lambda callback: callback.data == "kavkaz_info")
async def profile_driver(callback: CallbackQuery):


    kb_inline = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Озеро Кезеной  💧", callback_data="kezinoy"),
         InlineKeyboardButton(text="Аргунское ущелье ⛰️", callback_data="argunskoe_uschele"),],

        [InlineKeyboardButton(text="Шаройские башни 🌌", callback_data="sharoyskoe_bashni"),
         InlineKeyboardButton(text="Беной 🌳", callback_data="benoy"),],

        [InlineKeyboardButton(text="Сулакский каньон 🌉", callback_data="sulakskiy_kanon"),
         InlineKeyboardButton(text="Горы Ингушетии 🗻", callback_data="mountains")],

        [InlineKeyboardButton(text="Владикавказ 🏔️", callback_data="vladikavkaz"),
         InlineKeyboardButton(text="Ушалойские башни", callback_data="ushaloi")],


        [InlineKeyboardButton(text="Вернутся в назад 👈", callback_data="start")]
    ])



    await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id= callback.message.message_id)
    await callback.message.answer(text=kavkaz_highlights, caption=car_description, reply_markup=kb_inline)


# Озеро Кезеной
# Аргунское ущелье
# Шаройское ущелье
# Беной
# Сулакский каньон
# Горы Ингушетии 
# Владикавказ