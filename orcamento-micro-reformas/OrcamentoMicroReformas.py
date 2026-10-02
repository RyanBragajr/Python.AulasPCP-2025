print("------ Início do programa ------")
print("Calculadora de orçamento para micro-reformas\n")

while True:
    print("===== MENU DE SERVIÇOS =====")
    print("1 - Troca de Piso")
    print("2 - Pintura Geral")
    print("3 - Troca de Revestimento de Parede")
    print("4 - Ar-Condicionado")
    print("5 - Elétrica (troca de tomadas)")
    print("6 - Manutenção de Itens")
    print("7 - Sair")
    print("============================\n")

    try:
        tipoServico = int(input("Digite o número do serviço que deseja selecionar: "))
    except ValueError:
        print("Por favor, digite um número válido.\n")
        continue

    if tipoServico == 7:
        print("Encerrando o programa... Até logo!")
        break

    match tipoServico:
        case 1:
            print("Você selecionou: Troca de Piso")


            def calcularMircroReforma():
                print("Micro Reforma - Troca de Piso\n")
                # Pergunta sw terá troca de piso
                trocaPiso = input("Terá troca de piso? (Sim/Não): ")

                if trocaPiso == "não":
                    print("Não haverá troca de piso.")
                    return

                # Se sim, pergunta a area
                area = float(input("Insira Área em metros quadrados que será demolida: "))

                # Pergunta se terá demolição do piso Existente
                demolicao = input("Terá demolição de piso exstente? (Sim/Não): ").strip().lower()
                demolicaoPiso = 30.00
                custoDemolicao = 0

                if demolicao == "sim":
                    custoDemolicao = area * demolicaoPiso

                # Pergunta o Tipo de piso
                print("\nQual tipo de piso você prefere?")
                print("(A) Porcelanato Cimento Queimado")
                print("(B) Assoalho de Madeira")
                print("(C) Vinílico")
                print("(D) Laminado")

                tipoPiso = input("Escolha uma opção (A/B/C/D): ").strip().upper()

                # Inicializa o custo de piso da instalação
                custoPiso = 0

                if tipoPiso == "A":
                    valorPisoPorcelanatoMedio = 120
                    valorServicoInstalacaoPorcelanato = 90
                    custoPiso = (valorPisoPorcelanatoMedio + valorServicoInstalacaoPorcelanato) * area

                elif tipoPiso == "B":
                    valorPisoAssoalhoMadeiraMedio = 350
                    custoPiso = valorPisoAssoalhoMadeiraMedio * area

                elif tipoPiso == "C":
                    valorPisoVinilicoMedio = 80
                    valorInstalacaoPisoVinilico = 50
                    custoPiso = (valorPisoVinilicoMedio + valorInstalacaoPisoVinilico) * area

                elif tipoPiso == "D":
                    valorPisoLaminadoMedio = 70
                    valorIstalacaoPisoLaminado = 50
                    custoPiso = (valorPisoLaminadoMedio + valorIstalacaoPisoLaminado) * area

                else:
                    print("Opção Invalida.")
                    return

                # Calcula o Piso Total
                custoTotal = custoPiso + custoDemolicao

                # Exibe o Resultado
                print(f"\nCusto Total da troca de piso: R$ {custoTotal:.2f}")
                if custoTotal > 0:
                    print(f"Custo da demolição do piso existente: R$ {custoDemolicao:.2f}/n")

            # Chama a função pra executar o programa
            calcularMircroReforma()

        case 2:
            print("Você selecionou: Pintura Geral\n")

            def calcularPintura():
                print("Pintura Geral")
                print("Tipos de pintura disponíveis:")
                print("1. Branca Comum (R$ 15 / m²)")
                print("2. Colorida Comum (R$ 18 / m²)")
                print("3. Branca Acrílica (R$ 20 / m²) - Para áreas que entram em contato com água")
                print("4. Colorida Acrílica (R$ 25 / m²) - Para áreas que entram em contato com água")

                # Aviso sobre a diferença entre tintas comuns e acrílicas
                print(
                    "\nAtenção: As tintas acrílicas são recomendadas para áreas que podem entrar em contato com água, como cozinhas e banheiros.")

                # Inicializa o custo total
                custoTotal = 0

                # Coleta de informações sobre a área a ser pintada para cada tipo de tinta
                areaBrancaComum = 0
                areaColoridaComum = 0
                areaBrancaAcrilica = 0
                areaColoridaAcrilica = 0

                # Pergunta ao usuário quais tipos de pintura ele deseja e as áreas
                opcoes = input("\nEscolha os tipos de pintura que deseja (separados por vírgula, ex: 1,2,3,4): ")
                opcoes = opcoes.split(",")

                for opcao in opcoes:
                    opcao = opcao.strip()  # Remove espaços em branco
                    if opcao == "1":
                        areaBrancaComum = float(input("Informe a área a ser pintada com Branca Comum (em m²): "))
                        custoTotal += areaBrancaComum * 15  # Branca Comum
                    elif opcao == "2":
                        areaColoridaComum = float(input("Informe a área a ser pintada com Colorida Comum (em m²): "))
                        custoTotal += areaColoridaComum * 18  # Colorida Comum
                    elif opcao == "3":
                        areaBrancaAcrilica = float(input("Informe a área a ser pintada com Branca Acrílica (em m²): "))
                        custoTotal += areaBrancaAcrilica * 20  # Branca Acrílica
                    elif opcao == "4":
                        areaColoridaAcrilica = float(input("Informe a área a ser pintada com Colorida Acrílica (em m²): "))
                        custoTotal += areaColoridaAcrilica * 25  # Colorida Acrílica
                    else:
                        print(f"Opção {opcao} inválida. Ignorando.")

                # Exibe o resultado
                print(f"\nCusto total da pintura: R$ {custoTotal:.2f}\n")

            # Chama a função para executar o programa
            calcularPintura()

        case 3:
            print("Você selecionou: Troca de Revestimento de Parede\n")


            def calcularTrocaRevestimento():
                print("Troca de Revestimento ou Rejunte")

                demolicao = input("Haverá demolição de revestimento? (Sim/Não): ").strip().lower()

                custoDemolicao = 0

                # Se sim, informar area a ser demolida
                if demolicao == "sim":
                    areaDemolicao = float(input("Infomar m² demolido: "))
                    custoDemolicao = areaDemolicao * 30
                    print(f"Custo da demolição: R$ {custoDemolicao:.2f}")
                else:
                    areaDemolicao = 0

                # Opçoes
                print("\nOpções de revestimento:\n")
                print("(A) Revestimento Simples")
                print("(B) Revestimento Plus")
                print("(C) Ambos")

                opcaoRejunte = input("\nEscolha uma Opção (A/B/C): ").strip().upper()

                # Inicializa Variaveis
                areaSimples = 0
                areaPlus = 0

                if opcaoRejunte == "A":
                    areaSimples = float(input("\nInforme a área de troca para Revestimento Simples em m²: "))

                    # Valores Rev Simples
                    valorRevestimentoSimples = 55
                    valorInstalacaoSimples = 70
                    totalRevestimentoSimples = (valorRevestimentoSimples + valorInstalacaoSimples) * areaSimples
                    custoTotal = custoDemolicao + totalRevestimentoSimples

                elif opcaoRejunte == "B":
                    areaPlus = float(input("Informe a área de troca para Revestimento Plus em m²: "))

                    # Valores Rev Plus
                    valorRevestimentoPlus = 150
                    valorInstalacoPlus = 95
                    totalRevestimentoPlus = (valorRevestimentoPlus + valorInstalacoPlus) * areaPlus
                    custoTotal = custoDemolicao + totalRevestimentoPlus

                elif opcaoRejunte == "C":
                    areaSimples = float(input("Informe a área de troca para Revestimento Simples em m²: "))
                    areaPlus = float(input("Info3rme a área de troca para Revestimento Plus em m²: "))

                    valorRevestimentoSimples = 55
                    valorInstalacaoSimples = 70
                    totalRevestimentoSimples = (valorRevestimentoSimples + valorInstalacaoSimples) * areaSimples

                    valorRevestimentoPlus = 150
                    valorInstalacoPlus = 95
                    totalRevestimentoPlus = (valorRevestimentoPlus + valorInstalacoPlus) * areaPlus

                    custoTotal = custoDemolicao + totalRevestimentoSimples + totalRevestimentoPlus

                else:
                    print("Opção invalida.")
                    return

                print(f"\nCusto total da troca de revestimetno: R$ {custoTotal:.2f}\n")


            calcularTrocaRevestimento()
        case 4:
            print("Você selecionou: Ar-Condicionado\n")
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
                        total_9 = qtd_ate_9 * (
                                    valores_instalacao["até_9"]["equipamento"] + valores_instalacao["até_9"]["infra"])
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
            print(f"Custo total R$:{custo_total:.2f}\n")

        case 5:
            print("Você selecionou: Elétrica (troca de tomadas)\n")


            def calcularPrecoTomadas():
                print("Informe a quantidade de cada tipo de tomada a ser trocada:\n")

                tomadas10a = int(input("Tomadas 10A: "))
                tomadas20a = int(input("Tomadas 20A: "))
                tomadasComAterramento = int(input("Tomadas com aterramento: "))

                # Preços médios fixos
                preco10a = 60
                preco20a = 95
                precoAterramento = 125

                # Cálculo por tipo
                total10a = tomadas10a * preco10a
                total20a = tomadas20a * preco20a
                totalAterramento = tomadasComAterramento * precoAterramento

                # Soma geral
                totalGeral = total10a + total20a + totalAterramento

                print("\n--- Estimativa de custo ---")
                print(f"Tomadas 10A ({tomadas10a}x R$ {preco10a}): R$ {total10a:.2f}")
                print(f"Tomadas 20A ({tomadas20a}x R$ {preco20a}): R$ {total20a:.2f}")
                print(
                    f"Tomadas com aterramento ({tomadasComAterramento}x R$ {precoAterramento}): R$ {totalAterramento:.2f}")
                print("------------------------------")
                print(f"Total geral: R$ {totalGeral:.2f}\n")

            # Executar função
            calcularPrecoTomadas()

        case 6:
            print("Você selecionou: Manutenção de Itens\n")

            quantAjuste = int(input('Digite a quantidade de manutenções que deseja realizar: '))

            # Função com as condições da cobrança da manutenção
            def valorManutencao(quantAjuste):
                diariaManutencao = 400
                ajusteDiaria = 4  # quantidade de ajustes por cobrança da diária
                if quantAjuste == 0:
                    print("Nenhum serviço realizado")
                else:
                    # Calcula quantas diárias são necessárias, sempre arredondando pra cima
                    quantidadeDiarias = (quantAjuste + ajusteDiaria - 1) // ajusteDiaria
                    valorTotal = quantidadeDiarias * diariaManutencao
                    print(f"Quantidade de diárias cobradas: {quantidadeDiarias}")
                    print(f"O valor da manutenção será de: R$ {valorTotal}\n")

            valorManutencao(quantAjuste)
        case _:
            print("Opção inválida. Por favor, selecione uma opção de 1 a 6.")
