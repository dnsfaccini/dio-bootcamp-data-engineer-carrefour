#######################################################
## LISTAS - São mutaveis

# Cria lista
lista_animal = ['cachorro','gato','elefante']

# Imprime Lista
print(lista_animal)

# Imprime Lista com valor na posição 1
print(lista_animal[1])

# Insere valor na lista
lista_animal.append('lobo')

# Retorna a quantidade de elementos da lista
print(len(lista_animal))

# Substitui o valor na posicao 0 por outro
lista_animal[3] = 'arara'

# Tira o ultimo elemento da lista
lista_animal.pop()

# Tira o elemento de posicao 2 da lista
lista_animal.pop(2)

# Tira o elemento cachorro da lista
lista_animal.remove('cachorro')

# Ordena lista
lista_animal.sort()

# Reverte a ordenação
lista_animal.reverse()

# Percorre a lista
for x in lista_animal:
    print(x)

# Verifica se existe elemento na lista
if 'gato' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')

# Cria lista
lista = [1,3,5,7]

# Imprime Lista
print(lista)

# Soma a lista
print(sum(lista))

# Imprime menor valor
print(min(lista))

# Imprime maior valor
print(max(lista))

# Repete os valores
nova_lista = lista_animal * 3
print(nova_lista)

#######################################################
## Tuplas - São imutaveis

# Cria tupla
tupla = (1,10,12,14)

# Imprime tupla
print(tupla)

# Acessa elemento na posicao 2
print(tupla[2])

# Retorna a quantidade de elementos da tupla
print(len(tupla))

# Converte lista para tupla
tupla_animal = tuple(lista_animal)
