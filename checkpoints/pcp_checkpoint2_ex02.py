print("=== Verificador de Tipo de Triângulo ===\n")

# Entrada dos lados
lado1 = int(input("Digite o 1º lado: "))
lado2 = int(input("Digite o 2º lado: "))
lado3 = int(input("Digite o 3º lado: "))

# Organizando os lados em ordem decrescente
lados = sorted([lado1, lado2, lado3], reverse=True)
a, b, c = lados  # a é o maior, c o menor

print(f"\nLados organizados (maior para menor): {a}, {b}, {c}")

# Verificando se forma triângulo
if a >= (b + c):
    print("\n❌ Não forma um triângulo.")
else:
    # Classificação quanto aos ângulos
    if a**2 == b**2 + c**2:
        print("\n📐 Triângulo Retângulo")
    elif a**2 > b**2 + c**2:
        print("\n📏 Triângulo Obtusângulo")
    elif a**2 < b**2 + c**2:
        print("\n📎 Triângulo Acutângulo")

    # Classificação quanto aos lados
    if a == b == c:
        print("🔺 Triângulo Equilátero (3 lados iguais)")
    elif a == b or b == c or a == c:
        print("🔻 Triângulo Isósceles (2 lados iguais)")
    else:
        print("🔻 Triângulo Escaleno (3 lados diferentes)")
