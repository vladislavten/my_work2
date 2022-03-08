# 31.2 Регулярные выражения: модуль re и его методы

# Задача 1. Скороговорка

# import re
#
# text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
#
# result = re.match('wo', text)
# print('Поиск шаблона в начале строки:',result)
#
#
# result = re.search('wo', text)
# print('Поиск первого найденного совпадения по шаблону:', result)
# print('Содержимое найденной подстроки:', result.group(0))
# print('Начальная позиция:', result.start())
# print('Конечная позиция:', result.end())
#
#
# result = re.findall('wo', text)
# print('Список всех упоминаний шаблона:', result)
#
# result = re.sub('wo', 'ЗАМЕНА', text)
# print('Текст после замены:', result)


# Задача 2. Экранирование спецсимволов

# import re
#
# text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
#
# result = re.findall(r'\\wwood\+\?', text)
# print(result)


# 31.3 Регулярные выражения: шаблоны
# Задача 1. Согласные

# import re
#
# text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
#
# result = re.findall(r'\b[aeiouAEIOU]\w*', text)    # \b - начинать с начала слова,  [aeuio] - С каких букв будет начинаться, \w+ все слово целиком
# print(result)
#
# result = re.findall(r'\s\b[^aeiouAEIOU]\w+', text)    # \b - начинать с начала слова,  [aeuio] - С каких букв будет начинаться, \w+ все слово целиком
# print(result)



# Задача 2. Даты

# import re
#
#
# text = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
#
# result = re.findall('\d\d-\d\d-\d\d\d\d', text)
# result2 = re.findall('\w+ \d\d-\d\d\d\d', text)
# print(result)
# print(result2)



# 31.4 Основы парсинга: модуль request и формат JSON

# Задача 1. Звёздные войны

# import requests, json
#
# my_req = requests.get('https://swapi.dev/api/people/3/')
#
# print(my_req.text)
#
# data = json.loads(my_req.text, )  # Десерализация JSON
# data['name'] = 'Vladislav'
# print(data)
#
# with open('My_test.json', 'w') as file:
#     json.dump(data, file, indent=4) #Серализация JSON
#
#
# my_req2 = requests.get('https://swapi.dev/api/planets/8/')
# print(my_req2.text)
#
# data2 = json.loads(my_req2.text)
# print(data2)


