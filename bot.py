import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

# Инициализируем логгер
logger = logging.getLogger(__name__)

async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запустить бота'),
        BotCommand(command='/help',
                   description='Помощь по работе с ботом')]

    await bot.set_my_commands(main_menu_commands)

# Функция конфигурирования и запуска бота
async def main():
    logging.basicConfig(level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.startup.register(set_main_menu)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
