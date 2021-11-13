shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код

enter = input('Название детали: ')
count_detail = 0
summ = 0
for i in range(len(shop)):
        if shop[i][0] == enter:
                count_detail += 1
                summ += shop[i][1]
print('\nКол-во деталей:', count_detail)
print('Общая стоимость:', summ