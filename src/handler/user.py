from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# дочерный роутер
router = Router()


# встреча бота
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Саламалейкум")


