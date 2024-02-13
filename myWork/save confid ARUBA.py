
#Создатель Тен Владислав Сергеевич +77017107829

import time, paramiko, datetime
from colorama import init, Fore

init()

def execute_commands_ssh(ip, username, password, commands):
    '''
    Функция для сохранения конфигурации коммутатора ARUBA
    '''
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print('Время:', datetime.datetime.now())
        print('Опрашивается IP адрес:', ip)
        date = str(datetime.datetime.now().date())
        # print(date)
        # Connect to the switch
        ssh_client.connect(ip, username=username, password=password, timeout=5)


        # Create shell
        shell = ssh_client.invoke_shell()

        # Wait for the shell to open
        time.sleep(1)

        shell.send(' show running-config | include hostname' + '\n')
        time.sleep(1)
        hostname = shell.recv(65535).decode("utf-8")
        # print(hostname)

        if hostname.split()[-3]:
            print('Имя коммутатора: ', hostname.split()[-3].strip('"'))

        # Send commands
        for command in commands:
            shell.send(command + '\n')
            time.sleep(1)

        for com in comm2:
            shell.send(com + ip + '_' + hostname.split()[-3].strip('"') + '_config_' + date +'\n')
            time.sleep(1)

        # Wait for the commands to execute
        time.sleep(1)

        # Read output
        output = shell.recv(65535).decode("utf-8")

        return output
    except Exception as e:
        return str(e)
    finally:
        ssh_client.close()

with open('ips.txt', 'r') as ips:
    for ip in ips:
        if __name__ == "__main__":
            # ip = "10.10.16.23"
            username = "admin"
            password = "Pa$$w0rd"
            commands = [" conf t"]
            comm2 = [' tftp 172.16.112.182 put startup-config ']
            output = execute_commands_ssh(ip[:-1], username, password, commands)
            time.sleep(1)
            if output == 'timed out':
                print(Fore.RED + 'Коммутатор отключен или IP адрес задан не верно' + Fore.RESET)
            else:
                print(Fore.GREEN + 'Конфигурация успешно сохранена' + Fore.RESET)
            print()



# if __name__ == "__main__":
#     ip = "10.10.16.23"
#     username = "admin"
#     password = "Pa$$w0rd"
#     commands = [" conf t"]
#     comm2 = [' tftp 172.16.112.182 put startup-config ']
#     output = execute_commands_ssh(ip, username, password, commands)
#     print('Конфигурация успешно выгружена')


