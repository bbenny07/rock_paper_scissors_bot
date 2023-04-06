from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton =     KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)
yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

# ------- Создаем игровую клавиатуру без использования билдера -------

button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_paper],
                                    [button_rock],
                                    [button_scissors]],
                                    resize_keyboard=True)