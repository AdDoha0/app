from aiogram.filters import Command
from aiogram.types import (Message, InlineKeyboardMarkup,
                           InlineKeyboardButton, CallbackQuery, FSInputFile)
from aiogram import Router

import json as js





def create_back(back_menu: str, text: str = "вернутся назад 👈") -> InlineKeyboardMarkup:
    "Создает клавиатуру для возврата назад"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text, callback_data=back_menu)],
    ])

    return kb



class ReturnInfoJson:
     "Класс для получения информации о месте из JSON-объекта"

     def __init__(self, id: int):
         self.id = id                   # id места в JSON-объекте
         with open(r'data\inf_kavkaz.json', 'r', encoding='utf-8') as file:

            data = js.load(file)
            places = data["kavkav"] # Массив мест в JSON-объекте
            place_id = next(place for place in places if place["id"] == id) # Находим место по id
            photo_path = place_id["photo_path"] # Путь к фото места

            # сохраняем информацию о месте в переменные
            self.name = place_id["name"]
            self.description = place_id["description"]
            self.photo = FSInputFile(photo_path)






class callback_handker_kavkaz():
    "Класс для обработки коллбэков, места Кавказ"
    def __init__(self, id_js_object: int, callback_data: str, router: Router):
        self.js_object = ReturnInfoJson(id_js_object)  # Информация о месте из JSON-объекта
        self.callback_data = callback_data # Коллбэк-данные
        self.router = router
        self.register_handlers()

    def register_handlers(self):
        # Здесь регистрируем обработчик коллбэка
        self.router.callback_query(lambda callback: callback.data == self.callback_data)(self.callback_processing)


    async def callback_processing (self, callback: CallbackQuery):

        await callback.message.bot.delete_message(chat_id=callback.message.chat.id,     # удаляем предыдущее сообщение
                                                  message_id=callback.message.message_id)

        await callback.message.answer_photo(   # отправляем фото и описание места
            photo=self.js_object.photo,
            caption=self.js_object.description,
            reply_markup=create_back("kavkaz_info")
        )