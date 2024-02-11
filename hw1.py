from aiogram import Bot, Dispatcher, types, executor
from config import token 
import random


secret_number = random.randint(1, 3)

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands='play')
async def play(message:types.Message):
    await message.answer("Я загадал число от 1 до 3 угадайте")


@dp.message_handler()
async def guess_number(message: types.Message):
    guess = int(message.text)
    if guess == secret_number:
        await message.answer("Правильно вы отгадали")
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    else:
        await message.answer("Не угадали")
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

executor.start_polling(dp)