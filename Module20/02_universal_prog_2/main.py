# TODO здесь писать код

def i_prime(n):
    return [num for num in range(2, len(n)) if 0 not in [num % i for i in range(2, int(num / 2) + 1)]]

######### переменные на выбор:
text = 'О Дивный Новый мир!'
# text = ('й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к')
# text = [100, 200, 300, 'буква', 0, 2, 'а']
# text = {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}
################################
lst = i_prime(text)
print([text[index] for index in lst])