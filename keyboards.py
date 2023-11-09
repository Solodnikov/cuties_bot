from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from lexicon.lexicon import LEXICON_RU


# buttons
cat_button = KeyboardButton(text=LEXICON_RU['cat'])
dog_button = KeyboardButton(text=LEXICON_RU['dog'])
fox_button = KeyboardButton(text=LEXICON_RU['fox'])

# keyboard
keyboard = ReplyKeyboardMarkup(
    keyboard=[[cat_button,
               dog_button,
               fox_button]],
    resize_keyboard=True,
)
