from __future__ import print_function
import conf
from aiogram import Bot, Dispatcher, executor, types

import os.path
import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import conf

TOKEN = conf.BOT
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1lHVGusRqFrQb4FeMB-mPC83tYWmncJwe-H1ZZG7a7Wk'
SAMPLE_SPREADSHEET_ID = conf.SHEETS
SAMPLE_RANGE_NAME = 'Ответы на форму (1)!A2:H10000'

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(f'Проверить отчёт')
    markup.add(item1)
    await bot.send_message(user_id, f'Привет {user_name} 👋! \nЯ готов сформировать отчет. Введите /start ', reply_markup=markup)


@dp.message_handler(commands=['mop'])
async def mop_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    #############################################

    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            # print('%s, %s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4], row[5]))
            # print((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            # today = datetime.date.today()
            # formatted_date = today.strftime("%d.%m.%Y")
            # # print(formatted_date == row[0][0:10])
            # text = row[0].split(" ")
            # print(text[0] == formatted_date)
            await bot.send_message(user_id, f'%s, %s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4], row[5]))

    except HttpError as err:
        print(err)

    #############################################

@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(f'Проверить отчёт')
    markup.add(item1)
    if message.chat.type == "private":
        if message.text == f'Проверить отчёт':
            """Shows basic usage of the Sheets API.
                Prints values from a sample spreadsheet.
                """
            creds = None
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

            try:
                service = build('sheets', 'v4', credentials=creds)

                # Call the Sheets API
                sheet = service.spreadsheets()
                result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range=SAMPLE_RANGE_NAME).execute()
                values = result.get('values', [])

                if not values:
                    print('Данных нет')
                    await bot.send_message(user_id, 'Данных нет')
                    return
                flg = False
                for row in values:
                    # Print columns A and E, which correspond to indices 0 and 4.
                    # print('%s, %s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4], row[5]))
                    # print((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                    today = datetime.date.today()
                    formatted_date = today.strftime("%d.%m.%Y")
                    # print(formatted_date == row[0][0:10])
                    text = row[0].split(" ")
                    # print(text[0] == formatted_date)

                    if text[0] == formatted_date:
                        # await bot.send_message(user_id,
                        #                    f'%s, %s, %s, %s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4],
                        #                                                         row[5], row[6], row[7]))
                        await bot.send_message(user_id, f'Менеджер: {row[1]}\n'
                                                        f'Дата {row[2]}\n'
                                                        f'Кол-во взятых в работу заявок за сегодня (в цифрах): {row[3]}\n'
                                                        f'Кол-во успешных звонков за сегодня (дозвонов) в цифрах: {row[4]}\n'
                                                        f'Сколько человек записали на консультацию (в цифрах): {row[5]}\n'
                                                        f'Количество продаж: {row[6]}\n'
                                                        f'Сумма продаж: {row[7]}', reply_markup=markup)
                        flg = True
                        print('Бот использовался,', user_full_name)

                if not flg:
                    await bot.send_message(user_id, 'За сегодня отчётов не найдено')
                    print('Бот использовался,', user_full_name)

                flg = False
            except HttpError as err:
                print(err)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)


