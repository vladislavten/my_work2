## Задача 7. Текстовый калькулятор 2 
Модифицируйте задачу про калькулятор: условие задачи остается тем же, но теперь пользователю должно выводиться сообщение с ошибочной строкой на экран с предложением её исправить. 


#### Пример 1:
````
Содержимое файла calc.txt
100 + 34
10 +* 3
23 / 4

Содержимое консоли:
Обнаружена ошибка в строке: 10 +* 3   Хотите исправить? да
Введите исправленную строку: 10 + 3

Сумма результатов: 152.75
````

#### Пример 2:
````
Содержимое файла calc.txt
100 + 34
10 +* 3
20 -* 2
23 / 4

Содержимое консоли:
Обнаружена ошибка в строке: 10 +* 3   Хотите исправить? нет
Обнаружена ошибка в строке: 20 -* 2   Хотите исправить? да
Введите исправленную строку: 20 - 2

Сумма результатов: 157.75
````