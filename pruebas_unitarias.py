import unittest

def calcula_media(*args):
    return sum(args) / len(args)
    
class TestCalculaMedia(unittest.TestCase):
    def test_1(self):
        resultado = calcula_media(*[10, 10, 10])  # Desempaquetamos la lista
        self.assertEqual(resultado, 10)

    def test_2(self):
        resultado = calcula_media(*[5, 3, 4])  # Desempaquetamos la lista
        self.assertEqual(resultado, 4)

if __name__ == '__main__':
    unittest.main()