import os
import time

# Executa um ping para cada endereço contido no arquivo hosts.txt
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('verificando o ip: ', ip)
        print('-'*60)  # Cria linha para formatar saida no terminal
        os.system('ping -n 2 {}' .format(ip))
        print('-' * 60)  # Cria linha para formatar saida no terminal
        time.sleep(5) # Espera 5 segundo até a proxima execucao