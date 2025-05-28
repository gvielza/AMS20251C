import unittest
from utilidades import tiene_mayusculas_y_minusculas
class TestCadenas(unittest.TestCase):
    def test_mixta(self):
        self.assertTrue(tiene_mayusculas_y_minusculas("Hola"))

    def test_solo_mayusculas(self):
        self.assertFalse(tiene_mayusculas_y_minusculas("HOLA"))

    def test_solo_minusculas(self):
        self.assertFalse(tiene_mayusculas_y_minusculas("hola"))

    def test_vacia(self):
        self.assertFalse(tiene_mayusculas_y_minusculas(""))


if __name__ == '__main__':
    unittest.main()