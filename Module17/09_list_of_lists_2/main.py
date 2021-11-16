nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# TODO здесь писать код

result = [nice_list[i][x][y] for i in range(len(nice_list)) for x in range(3) for y in range(3)]

print('Ответ:', result)