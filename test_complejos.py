import unittest
from complejos import (division_complejos, prettyprinting, suma_complejos, resta_complejos,
                       multiplicacion_complejos, modulo_complejos, conjugado_complejos,
                       get_fase, get_polar_rep, get_cart_rep)


class TestFuncionesComplejos(unittest.TestCase):


    def test_suma_complejos(self):
        self.assertEqual(suma_complejos((1, 2), (3, 4)), (4, 6))
        self.assertEqual(suma_complejos((-1, -2), (-3, -4)), (-4, -6))
        self.assertEqual(suma_complejos((0, 0), (0, 0)), (0, 0))


    def test_resta_complejos(self):
        self.assertEqual(resta_complejos((5, 6), (3, 4)), (2, 2))
        self.assertEqual(resta_complejos((1, 2), (3, 4)), (-2, -2))
        self.assertEqual(resta_complejos((-5, -6), (-3, -4)), (-2, -2))


    def test_multiplicacion_complejos(self):
        self.assertEqual(multiplicacion_complejos((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(multiplicacion_complejos((0, 0), (5, 6)), (0, 0))
        self.assertEqual(multiplicacion_complejos((1, -1), (1, -1)), (0, -2))


    def test_division_complejos(self):
        self.assertEqual(division_complejos((1, 2), (3, 4)), (0.44, 0.08))
        self.assertEqual(division_complejos((1, 1), (1, -1)), (0.0, 1.0))
        with self.assertRaises(ValueError):
            division_complejos((1, 1), (0, 0))  # División por cero


    def test_modulo_complejos(self):
        self.assertAlmostEqual(modulo_complejos(3, 4), 5.0)
        self.assertAlmostEqual(modulo_complejos(-3, -4), 5.0)
        self.assertAlmostEqual(modulo_complejos(0, 0), 0.0)


    def test_conjugado_complejos(self):
        self.assertEqual(conjugado_complejos(1, 2), (1, -2))
        self.assertEqual(conjugado_complejos(-1, -2), (-1, 2))
        self.assertEqual(conjugado_complejos(0, 0), (0, 0))


    def test_get_fase(self):
        self.assertAlmostEqual(get_fase(1, 1), 45.0)
        self.assertAlmostEqual(get_fase(-1, 1), 135.0)
        self.assertAlmostEqual(get_fase(-1, -1), 225.0)



    def test_get_polar_rep(self):
        mod, fase = get_polar_rep(3, 4)
        self.assertAlmostEqual(mod, 5.0)
        self.assertAlmostEqual(fase, 53.13010235415598, places=10)

        mod, fase = get_polar_rep(-3, -4)
        self.assertAlmostEqual(mod, 5.0)
        self.assertAlmostEqual(fase, 233.13010235415598, places=10)

        mod, fase = get_polar_rep(0, 0)
        self.assertAlmostEqual(mod, 0.0)
        self.assertAlmostEqual(fase, 0.0)


    def test_get_cart_rep(self):
        self.assertEqual(get_cart_rep(5, 53.13010235415599), (3.0, 4.0))
        self.assertEqual(get_cart_rep(5, -53.13010235415599), (3.0, -4.0))
        self.assertEqual(get_cart_rep(0, 0), (0.0, 0.0))

    def test_prettyprinting(self):
        self.assertEqual(prettyprinting((3, 4)), "3 + 4i")
        self.assertEqual(prettyprinting((-3, -4)), "-3 - 4i")
        self.assertEqual(prettyprinting((0, 0)), "0 - 0i")


if __name__ == "__main__":
    unittest.main()