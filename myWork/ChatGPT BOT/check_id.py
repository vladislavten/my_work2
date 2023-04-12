
def check_id(user_id):
    """Проверка user_id на наличие в базе данных
    пользователей и внесение в файл ids.txt при их отсутствии"""
    flg = True
    with open('ids.txt', 'r') as file:
        for line in file:
            if str(user_id) == line.strip():
                flg = False
                print('такой пользователь уже существует')
                break

    if flg:
        with open('ids.txt', 'a') as file:
            file.write(f'{user_id}\n')
            print('добавлен новый пользователь')

