from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()

# Этот хэндлер будет срабатывать на команду "/delmenu"
# и удалять кнопку Menu c командами
# @router.message(Command(commands='delmenu'))
# async def del_main_menu(message: Message, bot: Bot):
#     await bot.delete_my_commands()
#     await message.answer(text='Кнопка "Menu" удалена')

@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])