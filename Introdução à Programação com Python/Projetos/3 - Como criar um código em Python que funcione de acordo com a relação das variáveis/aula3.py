################################################
##EXERCICIO_1

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Teceiro valor: '))
#
# if a > b and a > c:
#     print('o maior valor é {}'. format(a))
# elif b > a and b > c:
#     print('o maior numero é {}'.format(b))
# else:
#     print('o maior numero é {}'.format(c))
# print('final do programa')

####################################################
##EXERCICIO_2
#
# a = int(input('Entre com um valor: '))
# resto = a % 2
# if resto == 0:
#     print('numero é par')
# else:
#     print('numero é impar')

####################################################
##EXERCICIO_3

# a = int(input('Entre com primeiro valor: '))
# b = int(input('Entre com segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um numero Par')
# else:
#     print('Nenhum para foi digitado')

####################################################
##EXERCICIO_4

a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Voce digitou errado, digite novamente'))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Voce digitou errado, digite novamente'))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Voce digitou errado, digite novamente'))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Voce digitou errado, digite novamente'))

media = (a + b + c + d) / 4

print('A média: {}'.format(media))
