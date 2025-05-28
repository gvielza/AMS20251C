import unittest 
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()
        
    def test_sumar(self):
        self.assertEqual(self.calc.sumar(3, 2), 5)

        
    def test_restar(self):
        self.assertEqual(self.calc.restar(5, 3), 2)

    def test_multiplicar(self):
       self.assertEqual(self.calc.multiplicar(4, 3), 12)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)
if __name__ == '__main__':
    unittest.main()