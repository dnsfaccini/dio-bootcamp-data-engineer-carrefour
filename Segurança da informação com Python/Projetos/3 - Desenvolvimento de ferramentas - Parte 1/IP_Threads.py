import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco)
print(endereco + 100)

########################

ipDois = '192.168.0.1/24'

rede = ipaddress.ip_network(ip)

print(rede)

# Imprime cada endereço na rede

for ip2 in rede:
    print(ip2)