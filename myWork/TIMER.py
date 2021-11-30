import random
import time
start_time = time.time()
#####################################


lst = [random.randint(0, 9) for _ in range(100000)]

new_lst = []

for i in range(int(len(lst) / 2)):
    new_lst.append(tuple(lst[:2]))
    lst.remove(lst[0])
    lst.remove(lst[0])



##########################################
print("--- %s seconds ---" % (time.time() - start_time))
