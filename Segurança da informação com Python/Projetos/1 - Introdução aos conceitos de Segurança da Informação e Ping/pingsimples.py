# Importa pacote os (Pacote que executa recursos do sistema operacional)
import os

ip_ou_host = input('Digite um IP ou Host a ser verificado: ')

# Executa o comando ping do sistema operacional, com 6 pacotes e espera como parametro ip ou host
os.system('ping -n 6 {}'.format(ip_ou_host))

