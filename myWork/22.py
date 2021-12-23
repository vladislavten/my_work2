# Задача 1. Сисадмин
# import os
#
# folder = 'access'
# file_name = 'admin.bat'
#
# abs_path = os.path.abspath(os.path.join(folder, file_name))
# print(abs_path)
#
# rel_path = os.path.join(folder, file_name)
#
# print(rel_path)



# Задача 2. Содержимое

# import os
#
# path = 'C:\Python310'
#
# for i_elem in os.listdir(path):
#     print(os.path.join(path, i_elem))
#
# print(os.path.abspath(os.path.join(os.path.sep,'123') )) #пример работы os.path......


# Задача 3. Корень диска

import os

print('Корень диска:', os.path.abspath(os.path.sep))