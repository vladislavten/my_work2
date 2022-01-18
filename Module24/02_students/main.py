# TODO здесь писать код


class Student:
     def __init__(self, name, g_number, balls):
        self.name = name
        self.g_number = g_number
        self.balls = balls

     def middle_ball(self):
         result = sum(self.balls) / len(self.balls)
         lst_students[result] = self.name

lst_students = {}

st_1 = Student('Миша', 1, [44, 56, 64, 30, 56])
st_1.middle_ball()
st_2 = Student('Петя', 1, [45, 59, 78, 32, 63])
st_2.middle_ball()
st_3= Student('Гриша', 1, [44, 55, 64, 30, 56])
st_3.middle_ball()
st_4= Student('Влад', 1, [44, 32, 64, 44, 56])
st_4.middle_ball()
st_5= Student('Жандос', 1, [56, 89, 56, 23, 55])
st_5.middle_ball()
st_6= Student('Женя', 1, [55, 63, 21, 11, 56])
st_6.middle_ball()
st_7= Student('Ксюша', 1, [21, 55, 23, 30, 56])
st_7.middle_ball()
st_8= Student('Даша', 1, [44, 55, 36, 78, 56])
st_8.middle_ball()
st_9= Student('Ульяна', 1, [90, 10, 11, 30, 56])
st_9.middle_ball()
st_10= Student('Нелля', 1, [44, 55, 59, 37, 56])
st_10.middle_ball()

for ball, name in sorted(lst_students.items()):
    print(name, '-', ball)