import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.config import load_config

logger = logging.getLogger(__name__)

# Точка входа функции программы
async def main():
    # получение конфигов
    config = load_config('.env')

    # конфигурацмя всех логиров 
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    
    
    logger.info("Bot is starting")

    # сам бот и роутер
    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True) # Удаление прошлых не обработанных событий
    await dp.start_polling(bot) # Пуск бота


if __name__ == '__main__':
    asyncio.run(main())