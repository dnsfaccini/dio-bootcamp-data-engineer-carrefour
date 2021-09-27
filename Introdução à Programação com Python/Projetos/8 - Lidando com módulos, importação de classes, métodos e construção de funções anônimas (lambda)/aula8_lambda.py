contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))


subtracao = lambda a, b: a - b
soma = lambda a, b: a + b
print(subtracao(5, 10))
print(soma(5, 10))

# calculadora com dicionario e lambda
calculadora = {
    'soma': lambda a, b: a + b,
    'substracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

soma = calculadora['soma']
print(soma(10,5))