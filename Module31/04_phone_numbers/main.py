import re

phone_numbers = ['9999999999', '999999-999', '99999x9999']

for count, item in enumerate(phone_numbers):
    if re.search(r'\b[8, 9]\d{9}', item):
        print(count + 1, 'номер: Всё в порядке')
    else:
        print(count + 1, 'номер: не подходит')
