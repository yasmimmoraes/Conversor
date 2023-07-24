def obter_caracter_hexadecimal(valor):
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_para_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obter_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def obter_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)


def hexadecimal_para_decimal(hexadecimal):
    hexadecimal = hexadecimal.lower()
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicao = 0
    for digito in hexadecimal:
        valor = obter_valor_real(digito)
        elevado = 16 ** posicao
        equivalencia = elevado * valor
        decimal += equivalencia
        posicao += 1
    return decimal


def decimal_para_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal


def octal_para_decimal(octal):
    decimal = 0
    posicao = 0
    octal = octal[::-1]
    for digito in octal:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicao)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicao += 1
    return decimal


def decimal_para_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario


def binario_para_decimal(binario):
    posicao = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        multiplicador = 2**posicao
        decimal += int(digito) * multiplicador
        posicao += 1
    return decimal