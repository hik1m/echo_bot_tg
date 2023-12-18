from aiogram import Bot,Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '6636430603:AAEs1uEhzE9RN49P3qz9WcgienzIvl4g4Cs'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Хиким!\nНапиши мне что нибудь')

@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь, а'
        'я пришлю тебе твоё сообщение'
    )

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
             text='Данный тип апдейтов не поддерживается'
        )


if __name__== '__main__':
    dp.run_polling(bot)