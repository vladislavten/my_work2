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
# my_req = requests.get('https://www.breakingbadapi.com/api/deaths')
#
#
# data = json.loads(my_req.text)
# print(len(data))
# print(data)
#
# with open('Breaking_Bad.json', 'w') as file:
#        json.dump(data, file, indent=4)




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
# find_data = re.findall(r'(<h3 id=.*>)(.*?)(</h3>)', my_req.text)
# result = []
# for i in find_data:
#     result.append(i[1])
#
# print(result)






























