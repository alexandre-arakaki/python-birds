from unittest import TestCase

def soma(a, b):
    return a+b

class TestSoma(TestCase):
    def teste_soma(self):
        resultado = soma(1,3)
        self.assertEqual(4, resultado)