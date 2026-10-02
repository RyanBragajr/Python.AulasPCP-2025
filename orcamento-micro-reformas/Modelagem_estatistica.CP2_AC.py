# Valores fixos (padrão)
diaria_manutencao = 450

valores_instalacao = {
    "até_9": {"equipamento": 1500, "infra": 500},
    "até_15": {"equipamento": 1800, "infra": 700},
    "até_30": {"equipamento": 2200, "infra": 1000},
    "mais_30": {"equipamento": 3000, "infra": 1500}
}

# Início do programa
print("=== Sistema de Custos - Ar-Condicionado ===\n")

# Parte 1 - MANUTENÇÃO
manutencao = input("Haverá alguma manutenção de Ar-Condicionado existente? (Sim/Não): ").strip().lower()
custo_manutencao = 0

if manutencao == "sim":
    custo_manutencao = diaria_manutencao
    print(f"> Diária de manutenção aplicada: R$ {custo_manutencao:.2f}\n")
else:
    print("> Nenhuma manutenção será realizada.\n")

# Parte 2 - INSTALAÇÃO
instalacao = input("Haverá instalação de um novo Ar-Condicionado? (Sim/Não): ").strip().lower()
custo_instalacao = 0

if instalacao == "sim":
    print("\nEscolha os tipos de ambientes que deseja instalar (digite os números separados por vírgula):")
    print("1 - Ambientes até 9 m²")
    print("2 - Ambientes até 15 m²")
    print("3 - Ambientes até 30 m²")
    print("4 - Ambientes acima de 30 m²")

    opcoes = input("Opções escolhidas: ").strip().split(',')

    for opcao in opcoes:
        opcao = opcao.strip()
        if opcao == '1':
            qtd_ate_9 = int(input("Informe a quantidade para ambientes até 9 m²: "))
            total_9 = qtd_ate_9 * (valores_instalacao["até_9"]["equipamento"] + valores_instalacao["até_9"]["infra"])
            custo_instalacao += total_9
            print(f"Ambientes até 9 m² ({qtd_ate_9}): R$ {total_9:.2f}")
        elif opcao == '2':
            qtd_ate_15 = int(input("Informe a quantidade para ambientes até 15 m²: "))
            total_15 = qtd_ate_15 * (
                        valores_instalacao["até_15"]["equipamento"] + valores_instalacao["até_15"]["infra"])
            custo_instalacao += total_15
            print(f"Ambientes até 15 m² ({qtd_ate_15}): R$ {total_15:.2f}")
        elif opcao == '3':
            qtd_ate_30 = int(input("Informe a quantidade para ambientes até 30 m²: "))
            total_30 = qtd_ate_30 * (
                        valores_instalacao["até_30"]["equipamento"] + valores_instalacao["até_30"]["infra"])
            custo_instalacao += total_30
            print(f"Ambientes até 30 m² ({qtd_ate_30}): R$ {total_30:.2f}")
        elif opcao == '4':
            qtd_mais_30 = int(input("Informe a quantidade para ambientes acima de 30 m²: "))
            total_mais_30 = qtd_mais_30 * (
                        valores_instalacao["mais_30"]["equipamento"] + valores_instalacao["mais_30"]["infra"])
            custo_instalacao += total_mais_30
            print(f"Ambientes acima de 30 m² ({qtd_mais_30}): R$ {total_mais_30:.2f}")
        else:
            print(f"Opção {opcao} inválida. Ignorando.")

    # Mostrar custo total de instalação
    print(f"\n--- Custo Total de Instalação ---")
    print(f"Custo total de instalação: R$ {custo_instalacao:.2f}")

# Custo total final
custo_total = custo_manutencao + custo_instalacao
print(f"\n--- Custo Total Final ---")
print(f"Custo total R$:{custo_total:.2f}")

