# Entrada
total_dias = int(input("Digite sua idade em dias: "))

# Cálculo de Anos, Meses e Dias
anos = total_dias // 365
resto = total_dias % 365

meses = resto // 30
dias = resto % 30

# Resultado
print(f"\nVocê tem Aproximadamente:")
print(f"{anos} anos")
print(f"{meses} meses")
print(f"{dias} dias")