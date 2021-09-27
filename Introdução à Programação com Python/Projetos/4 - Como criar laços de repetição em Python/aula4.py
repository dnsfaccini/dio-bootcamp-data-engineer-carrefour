##################################################
## Loop FOR

##for x in range(101):
##    print(x)

##################################################
### Verifica numero primo

# a = int(input('Entre com um numero:'))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1
#         #div += 1
#
# if div == 2:
#     print('Numero é {} é´Primo' .format(a))
# else:
#     print('Numero {} não é´Primo'.format(a))

##################################################
## Imprime numeros primos de 1 a 100

# for num in range(101):
#
#     div = 0
#     for x in range(1, num+1):
#          resto = num % x
#          #print(x, resto)
#          if resto == 0:
#              div = div + 1
#              #div += 1
#     if div == 2:
#          print(num)

##################################################
## Imprime numeros primos em um range especifico

# a = int(input('Entre com um numero limite:'))
#
# for num in range(a):
#
#     div = 0
#     for x in range(1, num+1):
#          resto = num % x
#          #print(x, resto)
#          if resto == 0:
#              div = div + 1
#              #div += 1
#     if div == 2:
#          print(num)

##################################################
## Loop WHILE

# a = 0
# while a < 10:
#     print(a)
#     a = a + 1

##################################################

nota = int(input('Entre com uma nota:'))

while nota > 10:
    nota = int(input('Nota invalida. Entre com uma nota:'))
print(nota)

##################################################