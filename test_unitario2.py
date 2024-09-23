import unittest

def prueba(a, b):
    return a + b
    
class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(prueba(3, 4), 7)
        
    def test_suma_negativos(self):
        self.assertEqual(prueba(-3, 4), 1)
        
if __name__ == '__main__':
    unittest.main()