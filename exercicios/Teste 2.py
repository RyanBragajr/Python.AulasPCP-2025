def gerador_pseudo_aleatorio(seed, a=1664525, c=1013904223, m=2**32, n=10):

    numeros = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        numeros.append(x / m)  # Normaliza para o intervalo [0, 1)
    return numeros

# Exemplo de uso
seed = 42
quantidade = 10
numeros = gerador_pseudo_aleatorio(seed, n=quantidade)

print("Números pseudo-aleatórios:")
for i, num in enumerate(numeros):
    print(f"{i+1}: {num}")