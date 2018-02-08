

class Calculadora:

	def __init__(self, numero1, numero2):
		self.numero1 = numero1
		self.numero2 = numero2

	def soma(self):
    	return self.numero1 + self.numero2

    def subtrai(self):
        return self.numero1 - self.numero2

    def multiplica(self):
        return self.numero1 * self.numero2

    def divide(self):
        return self.numero1 / self.numero2

from calculadora import Calculadora
calc = Calculadora(128,2)
print('Soma:', calc.soma())
print('Subtração:', calc.subtrai())
print('Multiplicação:', calc.multiplica())
print('Divisão:', calc.divide())        


