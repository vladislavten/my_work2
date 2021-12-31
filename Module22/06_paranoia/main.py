# TODO здесь писать код
file = open('text.txt', 'w')

alpha = ' abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input().strip().lower()
print(s)
res = ''
for c in s:
    res += alpha[(alpha.index(c) + n) % len(alpha)]
print('Result: "' + res + '"')