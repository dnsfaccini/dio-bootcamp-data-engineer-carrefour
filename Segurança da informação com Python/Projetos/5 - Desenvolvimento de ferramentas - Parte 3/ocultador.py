## Ocultador de arquivo

import ctypes

# pasta = input('Digite o caminho da pasta a ser ocultada, exemplo: (C:/pasta)')

atributo_ocultar = 0x02

# Ocultar pasta
# retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

# Ocultar arquivo
retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')