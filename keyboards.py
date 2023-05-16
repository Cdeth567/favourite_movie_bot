from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


but = [KeyboardButton(text='Аннотация'),
       KeyboardButton(text='Обложка'),
       KeyboardButton(text='Актёры'),
       KeyboardButton(text='Год выпуска'),
       KeyboardButton(text='Жанр'),
       KeyboardButton(text='Не интересует')]
kb = ReplyKeyboardMarkup(row_width=1)
kb.add(*but)
