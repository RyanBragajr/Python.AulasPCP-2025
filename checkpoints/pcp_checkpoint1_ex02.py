# Entrada
numero = int(input("Digite um número até 999: "))

# Separação de centena, dezena e unidade. Operadores Aritmétivos; // = divisão inteira,* = multiplica, % = resto de divisão
centena = (numero // 100) * 100

dezena = ((numero % 100) // 10) * 10

unidade = numero % 10

# Resultado
print(f"\nCentena = {centena}")
print(f"Dezena = {dezena}")
print(f"Unidade = {unidade}")