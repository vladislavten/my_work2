# TODO здесь писать код
first_tour_file = open('first_tour.txt', 'r')

# for i in first_tour_file:
#     print(i.split())

# file = first_tour_file.read().split()

flg = True
data = {}
count = 0
ball = 0
players_id = []
place = 1
for i_elem in first_tour_file: # вытаскаиваю проходной бал и заполняю в словарь data игроков из файла first_tour.txt
    if flg:
        ball = i_elem
        flg = False
    else:
        data[i_elem.split()[2]] = [i_elem.split()[0], i_elem.split()[1]]

for i_player in data: #Считаю количество игроков у кого больше 80 баллов
    if i_player > ball:
        count += 1

first_tour_file.close()

#Записываю в файл second_tour.txt у кого больше 80 баллов
second_tour_file = open('second_tour.txt', 'w')
second_tour_file.write(str(count) + '\n')
second_tour_file.close()
second_tour_file = open('second_tour.txt', 'a')

for i in sorted(data, reverse=True): #Записываю в файл second_tour.txt победителей
    if count != 0:
        second_tour_file.write(str(place) + ') ' + data[i][1][:1] + '. ' + data[i][0] + ' ' + i + '\n')
        count -= 1
        place += 1

second_tour_file.close()

file = open('second_tour.txt', 'r')
data = file.read()
for i in data:
    print(i, end='')







# print(ball)
# print(data)
