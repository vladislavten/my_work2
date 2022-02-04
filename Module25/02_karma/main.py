import random
from random import randint, choice

karma = 500


def one_day():
    if random.randint(1, 10) == 1:
        choose_exception = choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
        with open('karma.log', 'a') as log:
            log.write(choose_exception + '\n')
    return randint(1, 7)


karma_person = 0
while True:
    if karma_person >= karma:
        break
    one_day()
    karma_person += one_day()
    print(karma_person)
