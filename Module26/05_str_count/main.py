import os


def generate_filenames():
    for dir_path, dir_names, file_names in os.walk('../01_num_squares'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                yield open(os.path.join(dir_path, file_name))


def cat_files(files):
    for f_name in files:
        for i_line in f_name:
            yield i_line


py_files = generate_filenames()
py_file = cat_files(py_files)
count = 0
empty = 0
for line in py_file:
    if line.startswith('\n') or line.startswith('\t') or line.startswith('#'):
        empty += 1
    else:
        count += 1
print(count, 'строк кода,', 'пустых строк :', empty)
