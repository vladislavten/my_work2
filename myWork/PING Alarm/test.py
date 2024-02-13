
from ping3 import ping, verbose_ping

def ping_ip(ip_address):
    # Пингуем IP-адрес и выводим результат
    response = ping(ip_address)
    if response is not None:
        print(f'Ping successful. Round-trip time: {response} ms')
    else:
        print('Ping failed.')

# Пример вызова функции для пинга IP-адреса 8.8.8.8
ping_ip('8.8.8.8')