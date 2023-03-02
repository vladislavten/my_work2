
import os
import time
import requests
import json
import random
import cv2
import pytesseract
from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import ContentType, message, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '6186799264:AAG6hLbwPk0DJiUXxQJu2dq4Vp5_0NHO-KM'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
get_link = 'https://api.telegram.org/bot'
get_file = 'https://api.telegram.org/file/bot' + TOKEN + '/'
counter = 0


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await bot.send_message(user_id, f'Привет {user_name} 👋! \nЯ помогу распознать текст с картинки.\n'
                                    f'Отправь мне фото или картинку из галереи для распознования текста.')


@dp.message_handler(content_types=["photo"])
async def process_photo(message: types.Message):
    global counter
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    file_id = message.photo[-1].file_id
    link = get_link + TOKEN + '/getFile?file_id=' + file_id
    response = requests.get(link)
    data = json.loads(response.text)
    link_to_photo = get_file + data['result']['file_path']
    rnd_file_name = random.randint(1000, 1000000)
    folder = (os.path.abspath('images'))  # local folder to save the image
    # folder = "D:\Python_Basic\myWork\Remover BG BOT"  # local folder to save the image
    response = requests.get(link_to_photo)
    await bot.send_message(user_id, f'Загружаю фото и начинаю обработку\nпожалуйста подождите ⏱️')
    with open(folder + f"\{rnd_file_name}image.jpg", "wb") as f:
        f.write(response.content)

    # # Чтение изображения
    img = cv2.imread(folder + f"\{rnd_file_name}image.jpg")

    # Конфигурация tesseract
    config = ('--psm 11')

    # # Распознание текста
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img, lang='rus+eng', config=config)

    await bot.send_message(user_id, f'{user_name}, вот ваш распознанный текст с картинки')
    await bot.send_message(user_id, text)
    print('готово')
    time.sleep(2)
    await bot.send_message(user_id, f' Нужно еще, {user_name}?\nПросто загрузите фотографию для распознавания текста')

    # time.sleep(3)
    # os.remove(folder + f"\{rnd_file_name}image.jpg")
    # os.remove(folder + f"\{rnd_file_name}out.png")


    counter += 1
    print(f'Бот был использован: {counter} раз(а)')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)


###########################


# import cv2
# import pytesseract
#
# # Чтение изображения
# img = cv2.imread('image3.jpg')
#
# # Конфигурация tesseract
# config = ('--psm 11')
#
# # Распознание текста
# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# text = pytesseract.image_to_string(img, lang='rus+eng', config=config)
#
# with open('text_from_image.txt', 'w', encoding='utf8') as f:
#     f.write(text)
# print(text)


