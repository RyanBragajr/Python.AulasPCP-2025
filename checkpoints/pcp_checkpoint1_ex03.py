# Entradas
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite os meses além dos anos: "))
dias = int(input("Digite os dias além dos meses: "))

# Cálculo do total de dias (considerando 1 ano = 365 dias, 1 mês = 30 dias)
total_dias = (anos * 365) + (meses * 30) + dias

# Resultado
print(f"\nVocê já viveu aproximadamente {total_dias} dias.")