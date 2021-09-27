lista = [1,10]
arquivo = open('teste.txt','r')
try:
    x = a
    numero = lista[3]
    divisao = 10 / 0

except ZeroDivisionError:
    print('Não é´possivel realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar uma indice invalido da lista')
except BaseException as ex:
    print('Erro desconhecido: {}'.format(ex))
else:
    print('Imprime quando não houver Exception')
finally:
    print('Sempre executa')
    arquivo.close()