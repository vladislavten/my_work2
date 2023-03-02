# !/usr/bin/env/ python3

import cgi
import psycopg2
from config import host, user, password, bd_name
import create_pdf

our_form = cgi.FieldStorage()
first_name = our_form.getfirst('first_name')
body_text = our_form.getfirst('body_text')
id_number = our_form.getfirst('id')

print('Content-type: text/html')
print()

try:
    # подключение к базе данных
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=bd_name
    )
    connection.autocommit = True

    # # Создание таблицы
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE tab(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             body_text varchar(50) NOT NULL);"""
    #     )
    #     # connection.commite() # Ручной коммит
    #
    #     print(f'Успешно создано')

    # Вставка в базу данных
    if first_name and body_text:
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO tab(first_name, body_text) VALUES
                ('{first_name}', '{body_text}');"""
            )
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT id FROM tab WHERE first_name = '{first_name}' and body_text = '{body_text}';"""
            )
            id_number = cursor.fetchone()[0]
        create_pdf.create(first_name, body_text, id_number)

        print(f'Ваши данные успешно занесены в базу данных под номером: {id_number}<br/>')
        #     # connection.commite() # Ручной коммит

    elif id_number:
        # Извлечение из базы данных
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT first_name, body_text FROM tab WHERE id = '{id_number}';"""
            )

            print(cursor.fetchone())
            print(f'<br><object data="/documents/служебная записка_{id_number}.pdf" type="application/pdf" width="800" height="700"><p>Ваш браузер не поддерживает отображение PDF-файлов,<a href="служебная записка_98.pdf">скачайте файл здесь</a>.</p></object>')
            # print(cursor.fetchone()[0])
            # print(f'Успешно извлечено')

    # # Удаление таблицы
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE tab;"""
    #     )
    #
    #     print(f'Успешно удалена')

except Exception as _ex:
    print('[INFO} Error while working with PostgreSQL', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] Connection closed')


