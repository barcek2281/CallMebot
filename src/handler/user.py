from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# дочерный роутер
router = Router()


# встреча бота
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Саламалейкум")


@router.message(Command("sex"))
async def process_ping_admins(message: Message):
    
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    members_count = await message.chat.get_member_count()
    await message.answer(text=f"Пользователь вызвал функцию: {message.from_user.first_name}\nВсего пользователей: {members_count}")

    admins = await message.bot.get_chat_administrators(chat_id)
    print(type(admins))
    if admins:
        await message.answer(' '.join([f'@{admin.user.username}' for admin in admins if admin.user.username]))
    else:
        await message.answer("Ничего не получилось")