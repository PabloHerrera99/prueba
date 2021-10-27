import unittest
from prueba import Prueba

class my_test(unittest.TestCase):
     def test_hola_mundo(self):
        prueba = Prueba()
        self.assertEqual(prueba.saludo(), 'Hola Mundo')

if __name__ == '__main__':
    unittest.main()
