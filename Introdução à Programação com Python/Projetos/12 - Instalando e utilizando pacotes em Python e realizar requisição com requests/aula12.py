##### no CMD
# pip --version (Mostra versão do pip)
# pip --help    (Mostra as opções de comando do pip)
# pip freeze    (Mostra os pacote que estão instalados)
# pip list      (Mostra os pacote que estão instalados)

# Instala o pacote requests
# pip install requests

import requests

response = requests.get('https://viacep.com.br/ws/04105000/json')
# Responde codigo de status
print(response.status_code)

#Retorna a consulta em formato json
print(response.json())

dados_cep = response.json()
print(dados_cep['logradouro'])