
import time
import logging
import random
import time


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, message, InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token='5704015463:AAGcBZcmrg94gwHEb6knQGBhoyKD_24PIrM')
dp = Dispatcher(bot=bot)
phrases = ['Отличный выбор 👍',
           'Думаю, это правильный выбор ☝️',
           'Хмм, будет интересно 😎',
           'Страно...🤔',
           'Вполне может быть 🧐',
           'Решать тебе, но мне кажется это уже перебор 😮‍💨',
           'Это смешно 😂',
           'Это печально 😭',
           'Чего чего??? 🤨',
           'Всё будет хорошо 😇',
           'да ты как в воду смотришь 😧',
           'мдэээ 🤬',
           'Может все таки еще раз подбросишь монетку? 😑']
coin = ['Орёл "Да"', 'Решка "Нет"']


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Подбрасываю монетку 🪙')
    markup.add(item1)
    await bot.send_message(user_id, '🪙')
    await bot.send_message(user_id, f'\nПривет {user_name}! \nЯ помогу тебе в решении важных вопросов!'
                                    f'\n1. Задай свой вопрос'
                                    f'\n2. Орёл "Да", Решка  "Нет"'
                                    f'\n3. Нажимай кпонку "Подбрасываю монетку 🪙"', reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Подбрасываю монетку 🪙')
    markup.add(item1)

    if message.chat.type == "private":
        if message.text == 'Подбрасываю монетку 🪙':
            coin_rnd = random.choice(coin)
            await bot.send_message(message.chat.id, 'Секундочку... ⏱️')
            time.sleep(1.5)
            await bot.send_message(message.chat.id, f'{coin_rnd}')
            if coin_rnd == coin[0]:
                with open('revers.webp', 'rb') as sticker:
                    await bot.send_sticker(message.chat.id, sticker)
            if coin_rnd == coin[1]:
                with open('avers.webp', 'rb') as sticker:
                    await bot.send_sticker(message.chat.id, sticker)
            time.sleep(1.5)
            await bot.send_message(message.chat.id, f'{random.choice(phrases)}')
            time.sleep(1.5)
            await bot.send_message(user_id, f'\n{user_name}! '
                                            f'\nЗадавай еще вопрос и жми на "Подбрасываю монетку 🪙"', reply_markup=markup)

        else:
            await bot.send_message(message.chat.id, f'Ваш вопросы был: "{message.text}"')
            time.sleep(1)
            coin_rnd = random.choice(coin)
            await bot.send_message(message.chat.id, 'Секундочку... ⏱️')
            time.sleep(1.5)
            await bot.send_message(message.chat.id, f'{coin_rnd}')
            if coin_rnd == coin[0]:
                with open('revers.webp', 'rb') as sticker:
                    await bot.send_sticker(message.chat.id, sticker)
            if coin_rnd == coin[1]:
                with open('avers.webp', 'rb') as sticker:
                    await bot.send_sticker(message.chat.id, sticker)
            time.sleep(1.5)
            await bot.send_message(message.chat.id, f'{random.choice(phrases)}')
            time.sleep(1.5)
            await bot.send_message(user_id, f'\n{user_name}! '
                                            f'\nЗадавай еще вопрос и жми на "Подбрасываю монетку 🪙"', reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)