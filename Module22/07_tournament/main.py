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
for i_elem in first_tour_file: # вытаскаиваю проходной бал и заполняю в словарь data игроков из файла first_tour.txt
    if flg:
        ball = i_elem
        flg = False
    else:
        data[i_elem.split()[2]] = [i_elem.split()[0], i_elem.split()[1]]

for i_player in data: #Считаю у кого больше 80 баллов
    if i_player > ball:
        count += 1


#Записываю в файл second_tour.txt у кого больше 80 баллов
second_tour_file = open('second_tour.txt', 'w')
second_tour_file.write(str(count) + '\n')
second_tour_file.close()
second_tour_file = open('second_tour.txt', 'a')

print(sorted(data, reverse=True))


for i in sorted(data, reverse=True):
    if count != 0:
        print(i)
        count -= 1

# for index, value in enumerate(data):
#     if index > count - 1:
#         second_tour_file.write(max(data) + '\n')








# print(ball)
# print(data)
