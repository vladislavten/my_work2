
from aiogram import Bot, Dispatcher, executor, types
import re


TOKEN = '6945869021:AAFqsS_KmxonR60-vHNSbjqHIlaOPOJl6F8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
get_link = 'https://api.telegram.org/bot'
get_file = 'https://api.telegram.org/file/bot' + TOKEN + '/'
counter = 0


def format_phone_number(phone_number):
    # Удаление всех нецифровых символов
    cleaned_number = re.sub(r'\D', '', phone_number)

    # Проверка наличия 11 цифр (стандартный формат номера телефона в Казахстане)
    if len(cleaned_number) == 11:
        # Проверка, начинается ли номер с "8" и замена на "7" в этом случае
        if cleaned_number.startswith('8'):
            cleaned_number = '7' + cleaned_number[1:]
        # Форматирование номера в виде ссылки
        formatted_number = f'https://wa.me/{cleaned_number}'
        return formatted_number
    else:
        return None


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await bot.send_message(user_id, f'Привет {user_name} 👋! \nЯ помогу сгенерировать ссылку на WhatsApp.'
                                    f'\nПросто отправь мне номер телефона в любом формате')


@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    print(message.text)

    if not any(char.isalpha() for char in message.text):
        formatted_link = format_phone_number(message.text)
        if formatted_link:
            await bot.send_message(user_id, f"Ссылка для WhatsApp: {formatted_link}")
        else:
            await bot.send_message(user_id, "Ошибка: Неправильный формат номера.")
    else:
        await bot.send_message(user_id, "Ошибка: Номер телефона не должен содержать буквы.")
        await bot.send_message(user_id, 'Просто отправь мне номер телефона в любом формате')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)

