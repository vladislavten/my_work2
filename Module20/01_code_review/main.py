students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])


my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)

# TODO исправить код

def f(dict):
    lst = []
    string = []
    for index, value in dict.items():
        lst.extend(value['interests'])
        string.extend(value['surname'])
    string = len(string)
    return lst, string


for i, value in students.items():
    print('ID студента', i, '— возраст', value['age'])


hobbies, ages = f(students)
print('Список интересов:', ' '.join(hobbies))
print('Общая длина всех фамилий:', ages)