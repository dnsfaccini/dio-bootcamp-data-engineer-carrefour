import socket

# Cria objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso')

host = 'localhost'
port = 5432

# Faz a ligação entre cliente e servidor
s.bind((host, port))
mensagem = '\nServidor: Olá Cliente !'

#Enquanto verdadeiro 1 = TRUE
while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)