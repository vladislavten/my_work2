import random
import time


if __name__ == '__main__':
    start_time = time.time()
    #####################################



    print('1')
    lst = [random.randint(0, 9) for _ in range(100000)]




    ##########################################
    print("--- %s seconds ---" % (time.time() - start_time))
