import conversoes
import conversor
import unittest


class TestConversiones(unittest.TestCase):
    def test_binario_decimal(self):
        esperado = 7
        actual = conversoes.binario_a_decimal("111")
        self.assertEqual(actual, esperado)

    def test_decimal_binario(self):
        esperado = "111"
        actual = conversoes.decimal_a_binario(7)
        self.assertEqual(actual, esperado)

    def test_octal_decimal(self):
        esperado = 123
        actual = conversoes.octal_a_decimal("173")
        self.assertEqual(actual, esperado)

    def test_decimal_octal(self):
        esperado = "173"
        actual = conversoes.decimal_a_octal(123)
        self.assertEqual(actual, esperado)

    def test_hexadecimal_decimal(self):
        esperado = 255
        actual = conversoes.hexadecimal_a_decimal("ff")
        self.assertEqual(actual, esperado)

    def test_decimal_hexadecimal(self):
        esperado = "ff"
        actual = conversoes.decimal_a_hexadecimal(255)
        self.assertEqual(actual, esperado)

    def test_obter_numero_decimal(self):
        valores = [
            {
                "base": "2",
                "numero": "111",
                "esperado": 7,
            },
            {
                "base": "8",
                "numero": "173",
                "esperado": 123,
            },
            {
                "base": "16",
                "numero": "f",
                "esperado": 15,
            },
        ]
        for valor in valores:
            esperado = valor["esperado"]
            actual = conversor.obter_numero_decimal(
                valor["base"], valor["numero"])
            self.assertEqual(actual, esperado)


if __name__ == "__main__":
    unittest.main()