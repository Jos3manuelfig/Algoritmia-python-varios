import unittest

class TestSumaPar(unittest.TestCase):
    def test_sum_par_existe_par(self):
        lista_numeros = [1, 2, 3, 4, 7]
        resultado = suma_par(lista_numeros, 6)  # 2 + 4 = 6
        self.assertTrue(resultado)

    def test_sum_par_no_existe_par(self):
        lista_numeros = [1, 2, 3, 4, 7]
        resultado = suma_par(lista_numeros, 10)  # No hay par que sume 10
        self.assertFalse(resultado)

    def test_sum_par_lista_vacia(self):
        lista_numeros = []
        resultado = suma_par(lista_numeros, 6)
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()