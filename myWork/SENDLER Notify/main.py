import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Ваши учетные данные для почты
sender_email = "kidalo87@mail.ru"
sender_password = "WXz0v7i8vddtE3vjcUs5"
receiver_email = "v.ten@anpz.kz"

# Создание объекта сообщения
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Привет из Python"

# Текст сообщения
body = "Привет! Это тестовое сообщение из Python."
message.attach(MIMEText(body, "plain"))

# Подключение к серверу mail.ru
server = smtplib.SMTP("smtp.mail.ru", 587)
server.starttls()
server.login(sender_email, sender_password)

# Отправка сообщения
server.sendmail(sender_email, receiver_email, message.as_string())

# Завершение работы с сервером
server.quit()
print('Сообщение успешно отправлено')
