# import random
# import time
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     #####################################
#
#
#
#     print('1')
#     lst = [random.randint(0, 9) for _ in range(100000)]
#
#
#
#
#     ##########################################
#     print("--- %s seconds ---" % (time.time() - start_time))


a = '!!!ТTС аренда серв мощностей и каналов связи v 2'
b = '!!!ТTС аренда серв мощностей и каналов связи v 2'

count = 0
for i in a:
    if i != b[count]:
        print(i, b[count])
    count += 1
