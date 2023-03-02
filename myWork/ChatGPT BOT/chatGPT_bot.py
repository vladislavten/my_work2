import os
import openai
import conf
from aiogram import Bot, Dispatcher, executor, types

openai.api_key = conf.GPT
TOKEN = conf.BOT
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await bot.send_message(user_id, f'Привет {user_name} 👋! \nЯ ChatGPT, можешь меня попросить о чём угодно')


@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    # Запись запросов
    with open('Requests_from_user.txt', 'a') as file:
        file.write(f'Имя пользователя {user_name}. Запрос пользователя: {message.text} \n')
    # Отправка текста запроса на id 856618521
    await bot.send_message(chat_id="856618521", text=f'User_id: '
                                                     f'{user_id} Имя пользователя {user_name}. '
                                                     f'Запрос пользователя: {message.text}')
    await message.answer("Подождите немного, идет обработка данных")

    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
    )
    # print(user_id)

    await bot.send_message(user_id, response['choices'][0]['text'])




# print(response['choices'][0]['text'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)