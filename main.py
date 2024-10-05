import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from src.database.config import create_db, drop_db
from src.config import load_config
from src.handler import user


logger = logging.getLogger(__name__)

# сам бот и роутер
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

async def on_startup(bot):
	run_param = False
	if run_param:
		await drop_db()

	await create_db()

async def on_shutdown(bot):
    print('Бот лег')

# Точка входа функции программы
async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    # получение конфигов
    # config = load_config('.env')

    # конфигурацмя всех логиров 
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    
    
    logger.info("Bot is starting")

    # добавление дочерних роутеров
    dp.include_router(router=user.router)

    await bot.delete_webhook(drop_pending_updates=True) # Удаление прошлых не обработанных событий
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) # Пуск бота


if __name__ == '__main__':
    asyncio.run(main())