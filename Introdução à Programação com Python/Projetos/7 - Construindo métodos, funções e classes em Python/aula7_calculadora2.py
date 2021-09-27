class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def substracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacaO(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


# Instanciando e acessando valores
calculadora = Calculadora()
print(calculadora.soma(10,2))
print(calculadora.substracao(12,2))
print(calculadora.multiplicacaO(5,10))
print(calculadora.divisao(10,10))
