import conversiones


def solicitar_datos_a_usuario():
    bases_soportadas = ["2", "8", "10", "16", ]
    base_origen = input("""
2  - Binário
8  - Octal
10 - Decimal
16 - Hexadecimal
Digite a base numérica de entrada: [2, 8, 10, 16]: """)
    if base_origen not in bases_soportadas:
        print("ERRO! Não é possível utilizar esta base numérica")
        return
    numero = input(
        f"Agora digite o valor que deverá ser convertido a partir da base numérica {base_origen}: ")
    base_destino = input("""
2  - Binário
8  - Octal
10 - Decimal
16 - Hexadecimal
Escolha a base númerica de saída desejada: [2, 8, 10, 16]: """)
    if base_destino not in bases_soportadas:
        print("ERRO! Não é possível utilizar esta base")
        return
    return (base_origen, numero, base_destino)


def obtener_numero_decimal(base_origen, numero):
    if base_origen == "2":
        return conversiones.binario_a_decimal(numero)
    elif base_origen == "8":
        return conversiones.octal_a_decimal(numero)
    elif base_origen == "10":
        return int(numero)
    elif base_origen == "16":
        return conversiones.hexadecimal_a_decimal(numero)


def convertir(numero, base_destino):
    if base_destino == "2":
        return conversiones.decimal_a_binario(numero)
    elif base_destino == "8":
        return conversiones.decimal_a_octal(numero)
    elif base_destino == "10":
        return int(numero)
    elif base_destino == "16":
        return conversiones.decimal_a_hexadecimal(numero)


if __name__ == '__main__':
    datos = solicitar_datos_a_usuario()
    # Comprobamos si los datos son correctos
    if datos:
        base_origen, numero, base_destino = datos
        # Para ahorrarnos código, vamos a convertir el número a decimal (sin importar la base de origen) y luego ese número
        # lo convertimos a la base de destino
        numero_decimal = obtener_numero_decimal(base_origen, numero)
        # Y a ese decimal lo convertimos a la base deseada
        resultado = convertir(numero_decimal, base_destino)
        print(resultado)