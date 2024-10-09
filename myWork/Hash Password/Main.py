import hashlib

def my_hash(text):
    return hashlib.sha3_256(text.encode()).hexdigest()


password = 'f4b999296ad484b981dcfc63ccc275db65ce299d3b55fbf2dace6ad9eb5998d1'

input_password = input('Пароль: ')

if password == my_hash(input_password):
    print('Вы авторизовались')
else:
    print('Пароль введен не правильно')


