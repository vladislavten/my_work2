import psycopg2
from config import host, user, password, bd_name

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
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             body_text varchar(50) NOT NULL);"""
    #     )
    #     # connection.commite() # Ручной коммит
    #
    #     print(f'Успешно создано')

    # Вставка в базу данных
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO users(first_name, body_text) VALUES
            ('{a}', '{b}');"""
        )
    #     # connection.commite() # Ручной коммит


    # # Извлечение из базы данных
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT body_text FROM users WHERE id = '1';"""
    #     )
    #
    #     print(cursor.fetchone())
    #     print(f'Успешно извлечено')

    # # Удаление таблицы
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )
    #
    #     print(f'Успешно удалена')

except Exception as _ex:
    print('[INFO} Error while working with PostgreSQL', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] Connection closed')

