import conversoes


def solicitar_dados_a_usuario():
    bases_soportadas = ["2", "8", "10", "16", ]
    base_origem = input("""
2  - Binário
8  - Octal
10 - Decimal
16 - Hexadecimal
Digite a base numérica de entrada: [2, 8, 10, 16]: """)
    if base_origem not in bases_soportadas:
        print("ERRO! Não é possível utilizar esta base numérica")
        return
    numero = input(
        f"Agora digite o valor que deverá ser convertido a partir da base numérica {base_origem}: ")
    base_destino = input("""
2  - Binário
8  - Octal
10 - Decimal
16 - Hexadecimal
Escolha a base númerica de saída desejada: [2, 8, 10, 16]: """)
    if base_destino not in bases_soportadas:
        print("ERRO! Não é possível utilizar esta base")
        return
    return (base_origem, numero, base_destino)


def obter_numero_decimal(base_origem, numero):
    if base_origem == "2":
        return conversoes.binario_para_decimal(numero)
    elif base_origem == "8":
        return conversoes.octal_para_decimal(numero)
    elif base_origem == "10":
        return int(numero)
    elif base_origem == "16":
        return conversoes.hexadecimal_para_decimal(numero)


def converter(numero, base_destino):
    if base_destino == "2":
        return conversoes.decimal_para_binario(numero)
    elif base_destino == "8":
        return conversoes.decimal_para_octal(numero)
    elif base_destino == "10":
        return int(numero)
    elif base_destino == "16":
        return conversoes.decimal_para_hexadecimal(numero)


if __name__ == '__main__':
    dados = solicitar_dados_a_usuario()
    # Comprobamos si los dados son correctos
    if dados:
        base_origem, numero, base_destino = dados
        # Para ahorrarnos código, vamos a convertir el número a decimal (sin importar la base de origen) y luego ese número
        # lo convertimos a la base de destino
        numero_decimal = obter_numero_decimal(base_origem, numero)
        # Y a ese decimal lo convertimos a la base deseada
        resultado = converter(numero_decimal, base_destino)
        print(resultado)