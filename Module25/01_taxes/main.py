class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


money = float(input('Введите ваше кол-во денег: '))
price_apartment = float(input('Введите стоимость квартиры: '))
apartment = Apartment(price_apartment)
if price_apartment + apartment.tax() < money:
    print('Налог: ', apartment.tax())
else:
    print('У вас не хватает денег: ', price_apartment + apartment.tax() - money)

price_car = float(input('Введите стоимость автомобиля: '))
car = Car(price_car)
if price_car + car.tax() < money:
    print('Налог: ', car.tax())
else:
    print('У вас не хватает денег: ', price_car + car.tax() - money)

price_countryHouse = float(input('Введите стоимость дачи: '))
countryHouse = CountryHouse(price_countryHouse)
if price_countryHouse + countryHouse.tax() < money:
    print('Налог: ', countryHouse.tax())
else:
    print('У вас не хватает денег: ', price_countryHouse + countryHouse.tax() - money)
