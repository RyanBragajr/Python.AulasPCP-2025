import secrets

def gerar_numeros_aleatorios(quantidade, minimo=0, maximo=100):
    """
    Gera uma lista de números totalmente aleatórios no intervalo [minimo, maximo]
    usando o módulo secrets (mais seguro e imprevisível).
    """
    numeros = []
    for _ in range(quantidade):
        num = secrets.randbelow(maximo - minimo + 1) + minimo
        numeros.append(num)
    return numeros

# Exemplo de uso

quantidade = 10
numeros = gerar_numeros_aleatorios(quantidade, minimo=1, maximo=100)

print("Números completamente aleatórios:")
for i, num in enumerate(numeros):
    print(f"{i+1}: {num}")

