# TODO здесь писать код


alpha = 'abcdefghijklmnopqrstuvwxyz'
move = 1
file = open('text.txt', 'r')
text_string = file.read().split('\n')
print('Содержимое файла text.txt:')
for i_elem in text_string:
    print(i_elem)
file.close()
print()
print('Содержимое файла cipher_text.txt:')
for i in text_string:
    res = ''
    for x in i:
        res += alpha[(alpha.index(x.lower()) + move) % len(alpha)]
    file_write = open('cipher_text.txt', 'a')
    file_write.write(res + '\n')
    move += 1
    file_write.close()

file_write = open('cipher_text.txt', 'r')
result = file_write.read().split()

for i_elem in result:
    print(i_elem)

