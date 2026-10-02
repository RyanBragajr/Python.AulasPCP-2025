print("=== Sistema de Cálculo de Transporte de Carga ===\n")

# Entrada de dados
estado = int(input("Informe o estado de destino do caminhão (1)SP (2)RJ (3)MG (4)PR (5)SC: "))
peso_toneladas = float(input("Informe o peso da carga (em toneladas): "))
codigo_carga = int(input("Informe o código da carga (10 a 40): "))

# Conversão de toneladas para kg
peso_kg = peso_toneladas * 1000
print(f"\n🔹 Peso da carga convertido: {peso_kg:.2f} kg")

# Cálculo do preço base da carga
if 10 <= codigo_carga <= 20:
    preco = peso_kg * 100
elif 21 <= codigo_carga <= 30:
    preco = peso_kg * 250
elif 31 <= codigo_carga <= 40:
    preco = peso_kg * 340
else:
    print("❌ Código de carga inválido!")
    preco = 0

# Exibir preço da carga
if preco > 0:
    print(f"💰 Preço base da carga: R$ {preco:.2f}")
else:
    exit()

# Definindo imposto por estado
if estado == 1:
    imposto_percentual = 0.35
elif estado == 2:
    imposto_percentual = 0.25
elif estado == 3:
    imposto_percentual = 0.15
elif estado == 4:
    imposto_percentual = 0.05
elif estado == 5:
    imposto_percentual = 0
else:
    print("❌ Estado inválido!")
    exit()

# Cálculo do imposto e valor total
valor_imposto = preco * imposto_percentual
valor_total = preco + valor_imposto

# Exibir resultados finais
print(f"🧾 Imposto aplicado: R$ {valor_imposto:.2f} ({imposto_percentual*100:.0f}%)")
print(f"📦 Valor total da carga com imposto: R$ {valor_total:.2f}")
