import unittest

def es_par(n):
    return n %2 ==0
    
    
class test_es_par(unittest.TestCase):
      def test_par_posi(self):
           self.assertTrue(es_par(4))
      def test_par_negativo(self):
           self.assertFalse(es_par(-3))

if __name__ =='__main__':
    unittest.main()

        