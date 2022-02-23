class Date:
    """
    Класс Дата
    Проверяяет правильность даты и выводит на экран
    правильно (10-12-2022)
    НЕ правильно (10, 20, 30)
    """

    def __init__(self, day: int, month: int, year: int):
        self.day, self.month, self.year = day, month, year

    def __str__(self) -> str:
        return f'День: {self.day}   Месяц: {self.month}   Год: {self.year}'

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, month, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        day, month, year = map(int, date.split('-'))
        date_obj = cls(day, month, year)
        return date_obj


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
