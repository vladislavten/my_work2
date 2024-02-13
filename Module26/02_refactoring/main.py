












import time, paramiko, datetime


def execute_commands_ssh(ip, username, password, commands):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        date = str(datetime.datetime.now().date())
        print(date)
        # Connect to the switch
        ssh_client.connect(ip, username=username, password=password, timeout=5)

        # Create shell
        shell = ssh_client.invoke_shell()

        # Wait for the shell to open
        time.sleep(1)

        shell.send(' show running-config | include hostname' + '\n')
        time.sleep(1)
        hostname = shell.recv(65535).decode("utf-8")
        print(hostname.split()[-3][1:-1])
        print()

        # Send commands
        for command in commands:
            shell.send(command + '\n')
            time.sleep(1)

        for com in comm2:
            shell.send(com + hostname.split()[-3][1:-1] + '_config_' + date +'\n')
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


if __name__ == "__main__":
    ip = "10.10.16.25"
    username = "admin"
    password = "Pa$$w0rd"
    commands = [" conf t"]
    comm2 = [' tftp 172.16.112.182 put startup-config ']
    output = execute_commands_ssh(ip, username, password, commands)
    print('Конфигурация успешно выгружена')
    # print(output)
    # print()
    # print(output.split()[-3])

    # switch_hostname = get_switch_hostname(ip, username, password)
    # print("Switch hostname:", switch_hostname)

