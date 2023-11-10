from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types import FSInputFile
from lexicon.lexicon import LEXICON_RU
from keyboards import keyboard
from aiogram import F
from utils import (get_cat_photo_url,
                   get_dog_photo_url,
                   get_fox_photo_url)
from constants import START_FOTO

# Инициализируем роутер уровня модуля
router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    photo = FSInputFile(START_FOTO)
    await message.answer_photo(photo)
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=keyboard)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


# хэндлер для кошечек
@router.message(F.text == LEXICON_RU['cat'])
async def get_some_cat(message: Message):
    cat_link = get_cat_photo_url()
    if cat_link:
        await message.answer('Вот кошечка!')
        await message.answer_photo(cat_link)
    else:
        await message.answer(
            'Ошибка! Получить картинку в данный момент не возможно.'
        )


# хэндлер для собачек
@router.message(F.text == LEXICON_RU['dog'])
async def get_some_dog(message: Message):
    dog_link = get_dog_photo_url()
    if dog_link:
        await message.answer('Вот собачка!')
        await message.answer_photo(dog_link)
    else:
        await message.answer(
            'Ошибка! Получить картинку в данный момент не возможно.'
        )


# хэндлер для лисичек
@router.message(F.text == LEXICON_RU['fox'])
async def get_some_fox(message: Message):
    fox_link = get_fox_photo_url()
    if fox_link:
        await message.answer('Вот лисичка!')
        await message.answer_photo(fox_link)
    else:
        await message.answer(
            'Ошибка! Получить картинку в данный момент не возможно.'
        )
