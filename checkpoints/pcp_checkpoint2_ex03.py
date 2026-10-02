print("=== Sistema de Cálculo de Salário ===\n")

# Entrada de dados
nome = input("Digite o seu nome: ")
print("Cargos disponíveis:\n 1 - Gerente\n 2 - Analista\n 3 - Assistente\n 4 - Estagiário")
cargo = int(input("Selecione seu cargo (Digite o número correspondente): "))
salario_base = float(input("Digite seu salário base (R$): "))
horas_extras = int(input("Quantas horas extras você trabalhou no mês?: "))
faltas = int(input("Quantos dias de falta você teve no mês?: "))
bonus_recebido = int(input("Você recebeu bônus? (1 - Sim | 2 - Não): "))

# Exibe salário base
print(f"\n💼 Funcionário: {nome}")
print(f"💰 Salário base: R$ {salario_base:.2f}")

# Função para calcular horas extras
def calcular_horas_extras(salario, horas):
    return 0.015 * salario * horas

# Função para calcular bônus com base no cargo
def calcular_bonus(recebeu_bonus, cargo):
    if recebeu_bonus == 1:
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
        else:
            print("❌ Cargo inválido!")
            return 0
    elif recebeu_bonus == 2:
        return 0
    else:
        print("❌ Resposta de bônus inválida!")
        return 0

# Função para calcular desconto por faltas
def calcular_desconto_faltas(salario, faltas):
    return 0.02 * salario * (faltas ** 2)  # penalidade aumenta com mais faltas

# Cálculos
valor_horas = calcular_horas_extras(salario_base, horas_extras)
valor_bonus = calcular_bonus(bonus_recebido, cargo)
valor_desconto = calcular_desconto_faltas(salario_base, faltas)
salario_final = salario_base + valor_horas + valor_bonus - valor_desconto

# Exibição dos cálculos
print(f"\n🕒 Horas extras: R$ {valor_horas:.2f}")
print(f"🎁 Bônus recebido: R$ {valor_bonus:.2f}")
print(f"📉 Desconto por faltas: R$ {valor_desconto:.2f}")
print(f"\n📌 Salário final do mês: R$ {salario_final:.2f}")
