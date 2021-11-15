# TODO здесь писать код
def sort(nums):
    for i in range(len(nums)):
        for x in range(i, len(nums)):
            if nums[x] < nums[i]:
                nums[x], nums[i] = nums[i], nums[x]

people_list = []
skates_list = []

skates = int(input('Кол-во коньков: '))
for i in range(skates):
    print('Размер', i + 1, 'пары:', end = ' ')
    size = input()
    skates_list.append(size)

people = int(input('\nКол-во людей: '))
for i in range(people):
    print('Размер ноги', i + 1, 'человека:', end = ' ')
    size = input()
    people_list.append(size)

sort(people_list)
sort(skates_list)

count = 0
for i in people_list:
    for x in skates_list:
        if i <= x:
            count += 1
            skates_list.remove(x)
            break

print('Наибольшее кол-во людей, которые могут взять ролики: ', count )
