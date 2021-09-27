import socket

# Crio objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso")

# Seto os parametros de host,porta, mensagem
host = 'localhost'
porta = 5433
mensagem = 'Olá Servidor !'

# Tento enviar e receber a mensagem
try:
    print('cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432)) # Empacota e envia para este host e porta

    dados, servidor = s.recvfrom(4096) # Recebe e espera uma resposta com 4096 bytes
    dados = dados.decode()             # Desempacota os dados
    print('Cliente: '+ dados)
finally:
    print('Cliente: Fechando a conexão')
    s.close() # Fecha a conexão