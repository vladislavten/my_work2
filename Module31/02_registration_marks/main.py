import re
numbers_car = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_car = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}\w{2}\d{2,3}', numbers_car)
taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', numbers_car)
print('Список номеров частных автомобилей:', private_car)
print('Список номеров такси:', taxi)

