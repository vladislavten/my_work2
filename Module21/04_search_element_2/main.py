# TODO здесь писать код

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(struct, key, deep):
    if deep == 0:
        return
    if key in struct:
        return struct[key]
    for i in struct.values():
        if isinstance(i, dict):
            result = find_key(i, key,deep - 1)
            if result:
                break
    else:
        result = None

    return result

find = input('Какой ключ ищем? ')
deep = int(input('Введите глубину: '))
result = find_key(site, find, deep)
if result:
    print(result)
else:
    print('Такого ключа в структуре сайта нет')