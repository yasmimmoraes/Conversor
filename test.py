import conversoes
import conversor
import unittest


class TestConversoes(unittest.TestCase):
    def test_binario_decimal(self):
        esperado = 7
        atual = conversoes.binario_para_decimal("111")
        self.assertEqual(atual, esperado)

    def test_decimal_binario(self):
        esperado = "111"
        atual = conversoes.decimal_para_binario(7)
        self.assertEqual(atual, esperado)

    def test_octal_decimal(self):
        esperado = 123
        atual = conversoes.octal_para_decimal("173")
        self.assertEqual(atual, esperado)

    def test_decimal_octal(self):
        esperado = "173"
        atual = conversoes.decimal_para_octal(123)
        self.assertEqual(atual, esperado)

    def test_hexadecimal_decimal(self):
        esperado = 255
        atual = conversoes.hexadecimal_para_decimal("ff")
        self.assertEqual(atual, esperado)

    def test_decimal_hexadecimal(self):
        esperado = "ff"
        atual = conversoes.decimal_para_hexadecimal(255)
        self.assertEqual(atual, esperado)

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
            atual = conversor.obter_numero_decimal(
                valor["base"], valor["numero"])
            self.assertEqual(atual, esperado)


if __name__ == "__main__":
    unittest.main()