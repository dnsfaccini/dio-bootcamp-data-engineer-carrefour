def contador_letras(lista_letras):
    contador = []
    for x in lista_letras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':

        lista = ['cachorro', 'gato']
        print(contador_letras(lista))