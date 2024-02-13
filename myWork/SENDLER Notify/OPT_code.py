from __future__ import print_function
import os.path
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '111T2E0l0zNaxq4r3rXjNIXfSVNjMxWRYKCM0oFcda1Q'
SAMPLE_RANGE_NAME = 'Лист1!A2:E'


def authorize_google_sheets():
    """Authorize access to Google Sheets API and return credentials."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def fetch_data_from_spreadsheet(service):
    """Fetch data from the specified Google Sheets."""
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    return values


def write_to_file(values):
    """Write license information to a file."""
    with open('body_mail.txt', 'w', encoding="utf-8") as file:
        for row in values:
            date = row[1].split('.')
            target_date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
            days_remaining = target_date - datetime.datetime.now()
            if days_remaining.days <= 45:
                if days_remaining.days < 0:
                    file.write(f'Лицензия {row[0]} истекла: {days_remaining.days * -1} день/дней назад\n')
                else:
                    file.write(f'Лицензия {row[0]} истекает через: {days_remaining.days} дней до {target_date}\n')


def send_email():
    """Send email notification with license information."""
    sender_email = "anpz_notify@mail.ru"
    sender_password = "SqN8cwA44fcTh7fBcJiy"
    receiver_email = "vlad.ten87@gmail.com"

    with open('body_mail.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "ОПОВЕЩЕНИЕ ПО ЛИЦЕНЗИЯМ АНПЗ"

    body = text
    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.mail.ru", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print('Сообщение успешно отправлено')


def main():
    while True:
        creds = authorize_google_sheets()
        try:
            service = build('sheets', 'v4', credentials=creds)
            values = fetch_data_from_spreadsheet(service)

            if not values:
                print('No data found.')
                return

            write_to_file(values)
            send_email()

            time.sleep(86400)

        except HttpError as err:
            print(err)


if __name__ == '__main__':
    main()
