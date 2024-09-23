import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


import unittest

class TestCirculo(unittest.TestCase):
    
    def test_area(self):
        c1 = Circulo(1)
        self.assertAlmostEqual(c1.area(), math.pi, places=5)
        
        c2 = Circulo(0)
        self.assertEqual(c2.area(), 0)
        
        c3 = Circulo(2.5)
        self.assertAlmostEqual(c3.area(), math.pi * 2.5**2, places=5)

    def test_perimetro(self):
        c1 = Circulo(1)
        self.assertAlmostEqual(c1.perimetro(), 2 * math.pi, places=5)
        
        c2 = Circulo(0)
        self.assertEqual(c2.perimetro(), 0)
        
        c3 = Circulo(2.5)
        self.assertAlmostEqual(c3.perimetro(), 2 * math.pi * 2.5, places=5)

if __name__ == '__main__':
    unittest.main()