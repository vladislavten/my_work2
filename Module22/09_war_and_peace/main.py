# TODO здесь писать код
import zipfile
archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
# archive.printdir()

archive.extractall() # Извлечь файл из архива
