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