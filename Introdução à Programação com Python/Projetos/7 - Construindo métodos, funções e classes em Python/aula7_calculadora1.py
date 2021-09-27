class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b


    def substracao(self):
        return self.valor_a - self.valor_b


    def multiplicacaO(self):
        return self.valor_a * self.valor_b


    def divisao(self):
        return self.valor_a / self.valor_b

# Instanciando e acessando valores
calculadora = Calculadora(10,2)
print(calculadora.soma())
print(calculadora.substracao())
print(calculadora.multiplicacaO())
print(calculadora.divisao())

# print(soma(1, 2))
# print(substracao(1, 2))
# print(multiplicacaO(1, 2))
# print(divisao(1, 2))
