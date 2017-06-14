import unittest



# Converter um número inteiro para para string pt-br
# Por extenso em padrão brasileiro
# Considerar conjunções


def extenso(numero):
    if (numero < 0):
        return 'menos ' + extenso(-numero)

    unidades = ["zero", "um", "dois", "três",
                "quatro", "cinco", "seis", "sete",
                "oito", "nove", "dez", "onze",
                "doze", "treze", "quatorze", "quinze",
                "dezesseis", "dezessete", "dezoito", "dezenove"]

    dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta',
               'setenta', 'oitenta', 'noventa']

    centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos',
                'quinhentos', 'seiscentos', 'setecentos',
                'oitocentos', 'novecentos']

    if numero < 20:
        return unidades[numero]
    elif numero < 100:
        if numero % 10 == 0:
            return dezenas[numero // 10 - 2]
        else:
            return dezenas[numero // 10 - 2] + ' e ' + extenso(numero % 10)
    elif numero == 100:
        return "cem"
    elif numero < 1000:
        return centenas[numero // 100 - 1] + ' e ' + extenso(numero % 100)
    elif numero == 1000:
        return 'mil'
    elif numero < 2000:
        if numero % 1000 < 100:
            return 'mil e ' + extenso(numero % 1000)
        else:
            return 'mil, ' + extenso(numero % 1000)
    elif numero < 1e6:
        if numero % 1000 == 0:
            return extenso(numero // 1000) + ' mil'
        else:
            if numero % 1000 < 100:
                return extenso(numero // 1000) + ' mil e ' + extenso(numero % 1000)
            else:
                return extenso(numero // 1000) + ' mil, ' + extenso(numero % 1000)

    raise ValueError('Número muito grande em módulo!')


class TestDojoMethods(unittest.TestCase):
    def test_numero_simples(self):
        self.assertEqual(extenso(1), "um")
        self.assertEqual(extenso(4), "quatro")
        self.assertEqual(extenso(5), "cinco")
        self.assertEqual(extenso(7), "sete")
        self.assertEqual(extenso(20), "vinte")

    def test_dezenas(self):
        self.assertEqual(extenso(11), "onze")
        self.assertEqual(extenso(15), "quinze")
        self.assertEqual(extenso(19), "dezenove")
        self.assertEqual(extenso(20), "vinte")
        self.assertEqual(extenso(30), "trinta")
        self.assertEqual(extenso(90), "noventa")

    def test_numero_composto(self):
        self.assertEqual(extenso(27), "vinte e sete")
        self.assertEqual(extenso(94), "noventa e quatro")

    def test_numero_negativo(self):
        self.assertEqual(extenso(-1), "menos um")
        self.assertEqual(extenso(-13), "menos treze")
        self.assertEqual(extenso(-42), "menos quarenta e dois")

    def test_numero_centenas(self):
        self.assertEqual(extenso(100), "cem")
        self.assertEqual(extenso(124), "cento e vinte e quatro")
        self.assertEqual(extenso(540), "quinhentos e quarenta")
        self.assertEqual(extenso(999), "novecentos e noventa e nove")

    def test_numero_milhares(self):
        self.assertEqual(extenso(1000), 'mil')
        self.assertEqual(extenso(1007), 'mil e sete')
        self.assertEqual(extenso(2048), 'dois mil e quarenta e oito')
        self.assertEqual(extenso(2000), 'dois mil')
        self.assertEqual(extenso(55000), 'cinquenta e cinco mil')
        self.assertEqual(extenso(55555), 'cinquenta e cinco mil, quinhentos e cinquenta e cinco')
        self.assertEqual(extenso(125327), 'cento e vinte e cinco mil, trezentos e vinte e sete')
        self.assertEqual(extenso(-678321), 'menos seiscentos e setenta e oito mil, trezentos e vinte e um')
        self.assertEqual(extenso(999999), 'novecentos e noventa e nove mil, novecentos e noventa e nove')

    def test_erro_valor(self):
        self.assertRaises(ValueError, extenso, 1000000)
        self.assertRaises(ValueError, extenso, 3.2e10)
        self.assertRaises(ValueError, extenso, 13.7e9)
        self.assertRaises(ValueError, extenso, -33.7e10)
        self.assertRaises(ValueError, extenso, float('INF'))

if __name__ == '__main__':
    unittest.main()

