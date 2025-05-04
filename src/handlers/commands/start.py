from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}!")
