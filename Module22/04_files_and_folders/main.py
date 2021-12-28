# TODO здесь писать код
import os

enter_path = 'C:\Python_Basic'

size = os.path.getsize(enter_path)
general_size = 0
count = 0
for i_elem in os.listdir(enter_path):
    general_size += os.path.getsize(os.path.join(enter_path, i_elem))
    count += 1

print(general_size)
print(count)