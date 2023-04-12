
from aiogram import Bot, Dispatcher, executor, types
import os
from rembg import remove
import time
import requests
import json
import random

TOKEN = '5938351022:AAG4uCXRba1HxZpOJ88jXRFq235WpdPsA5o'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
get_link = 'https://api.telegram.org/bot'
get_file = 'https://api.telegram.org/file/bot' + TOKEN + '/'
counter = 0


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await bot.send_message(user_id, f'Привет {user_name} 👋! \nЯ помогу удалить фон с фото 📷.'
                                    f'\nПросто отправь мне фото и своей галереи 🏞️')


@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    print(message.text)
    await bot.send_message(user_id, f'{user_name}! \nЯ не понимаю текстовые сообщения.'
                                    f'\nПросто отправь мне фото из вашей галереи 🏞️ для удаления фона')


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
    folder = "C:\Python_Basic\myWork\Remover BG BOT"  # local folder to save the image
    response = requests.get(link_to_photo)
    await bot.send_message(user_id, f'Загружаю фото и начинаю обработку\nпожалуйста подождите ⏱️')
    with open(folder + f"\{rnd_file_name}image.jpg", "wb") as f:
        f.write(response.content)


    with open(folder + f"\{rnd_file_name}image.jpg", "rb") as image_file:
        image_data = image_file.read()

    result = remove(image_data)

    with open(folder + f"\{rnd_file_name}out.png", "wb") as out:
        out.write(result)


    # print(file_id)
    with open(folder + f"\{rnd_file_name}out.png", 'rb') as removered_bg:
        await bot.send_message(user_id, f'{user_name}, вот ваше фото, с удаленным фоном')
        await bot.send_photo(chat_id=message.chat.id, photo=removered_bg)
        time.sleep(2)
        await bot.send_message(user_id, f' Нужно еще, {user_name}?\nПросто загрузите фотографию')

    # time.sleep(3)
    # os.remove(folder + f"\{rnd_file_name}image.jpg")
    # os.remove(folder + f"\{rnd_file_name}out.png")


    counter += 1
    print(f'Бот был использован: {counter} раз(а)')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)






# import os
# from rembg import remove
#
# input_path = os.path.join('C:\Python_Basic\myWork\Remover BG BOT', 'img.jpg')
# output_path = os.path.join('C:\Python_Basic\myWork\Remover BG BOT', 'output.png')
#
# with open(input_path, "rb") as image_file:
#     image_data = image_file.read()
#
# result = remove(image_data)
#
# with open(output_path, "wb") as out:
#     out.write(result)







# url = "https://api.telegram.org/file/bot5938351022:AAG4uCXRba1HxZpOJ88jXRFq235WpdPsA5o/photos/file_2.jpg"
# folder = "C:\Python_Basic\myWork\Remover BG BOT"  # local folder to save the image
# response = requests.get(url)
# with open(folder + "/image.jpg", "wb") as f:
#     f.write(response.content)
#
# time.sleep(10)
# os.remove(folder + '/image.jpg')