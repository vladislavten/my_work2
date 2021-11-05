# TODO здесь писать код

def detect(x, y, r):
  if x ** 2 + y ** 2 <= r ** 2:
    print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')

x = float(input('Введите координату Х: '))
y = float(input('Введите координату Y: '))
r = float(input('Введите радиус: '))
detect(x, y, r)
