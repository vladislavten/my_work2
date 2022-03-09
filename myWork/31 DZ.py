# Задача 1. Lorem ipsum

# import re
#
# text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit." \
#        "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis" \
#        "natoque penatibus et magnis dis parturient montes, nascetur" \
#        "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu," \
#        "pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo," \
#        "fringilla vel, aliquet nec, vulputate"
#
# result = re.findall(r'\b\w{4}\b', text)
# print(result)


# Задача 2. Регистрационные знаки


# import re
# numbers_car = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
#
# private_car = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}\w{2}\d{2,3}', numbers_car)
# taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}',numbers_car)
# print('Список номеров частных автомобилей:', private_car)
# print('Список номеров такси:', taxi)


# Задача 3. Во все тяжкие

# import json, requests
#
# my_req = requests.get('https://www.breakingbadapi.com/api/deaths')  # Список погибших
# general_death_req = requests.get('https://www.breakingbadapi.com/api/death-count')  # Парсинг общего числа смертей
# episodes_req = requests.get('https://www.breakingbadapi.com/api/episodes')
#
# data = json.loads(my_req.text)
# deathCount = json.loads(general_death_req.text)
# episodes = json.loads(episodes_req.text)
#
# number_of_deaths = max(data, key=lambda elem: elem['number_of_deaths'])
#
# list_of_death = list(map(lambda x: x['death'], data))
#
# episode_id = {}
# for i_elem in episodes:
#     if i_elem['episode'] == '13' and i_elem['season'] == '2':
#         episode_id = i_elem
#         break
#
# print('ID эпизода:', episode_id['episode_id'])
# print('Номер сезона:', number_of_deaths['season'])
# print('Номер эпизода:', number_of_deaths['episode'])
# print('Общее число смертей:', deathCount[0]['deathCount'])
# print('Список погибших:', ', '.join(list_of_death))
#
# result = {'episode_id': episode_id['episode_id'],
#           'season': number_of_deaths['season'],
#           'episode': number_of_deaths['episode'],
#           'deathCount': deathCount[0]['deathCount'],
#           'death:': list_of_death
#           }
#
# with open('Breaking_Bad.json', 'w') as file:
#     json.dump(result, file, indent=4)

# Задача 4. Телефонные номера

# import re
#
# phone_numbers = ['9999999999', '999999-999', '99999x9999']
#
#
# for count, item  in enumerate(phone_numbers):
#        if re.search(r'\b[8, 9]\d{9}', item):
#               print(count + 1, 'номер: Всё в порядке')
#        else:
#               print(count + 1, 'номер: не подходит')


# Задача 5. Пин-код

# import itertools
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
# print(list(itertools.combinations(numbers, 4)))


# Задача 6. Web scraping

# import requests, re
#
# my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
#
# data = my_req.text
# # print(data)
#
# ser = re.findall(r'<h3 id="\w+">CONTENTS</h3>', data)
# print(ser)
#
# ser = re.findall(r'<h3 id="\w">CONTENTS</h3>', data)
# <h3 id="contents>CONTENTS</h3>
#
# <h3 id="contents">CONTENTS</h3>
