import random
import string

tamanho = int(input('Digite o tamanho da senha que vc deseja '))

chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()-+=:?'

rnd = random.SystemRandom()

# Gera a senha randomica
print(''.join(rnd.choice(chars) for i in range(tamanho)))