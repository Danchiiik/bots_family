from aiogram import Bot, Dispatcher, executor, types
from decouple import config

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    print('Bot working ...')
    executor.start_polling(dp)

