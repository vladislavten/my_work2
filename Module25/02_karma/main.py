import random
from random import randint, choice
KARMA = 500


def one_day():
    karma_result = randint(1, 7)
    if random.choices((0, 1), (1 - 1 / 10, 1 / 10))[0] == 1:
        choose_exception = choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
        with open('karma.log', 'a') as log:
            log.write(choose_exception + '\n')
    return karma_result


karma_person = 0
while True:
    if karma_person >= KARMA:
        break
    one_day()
    karma_person += one_day()
    print(karma_person)