def pode_aprovar(idade, renda, valor, parcelas):
    """Verifica se o cliente atende os critérios para aprovação do empréstimo"""

    if idade < 18:
        return False  # Não pode aprovar se for menor de idade

    if valor > 15 * renda:
        return False  # Valor do empréstimo não pode ser maior que 15x a renda

    if parcelas < 3 or parcelas > 24:
        return False  # Parcelas fora do intervalo permitido

    return True


def calcular_juros(valor, parcelas):
    """Calcula o valor total com base na taxa de juros mensal e número de parcelas"""

    if parcelas <= 6:
        taxa = 0.05  # 5% ao mês
    elif 7 <= parcelas <= 12:
        taxa = 0.08  # 8% ao mês
    else:
        taxa = 0.10  # 10% ao mês

    valor_total = valor * (1 + taxa) ** parcelas
    return valor_total


def calcular_parcela(valor_total, parcelas):
    """Retorna o valor de cada parcela"""
    return valor_total / parcelas


def main():
    print("=== SIMULADOR DE EMPRÉSTIMO ===\n")

    # Entrada de dados do cliente
    nome = input("Nome do cliente: ")
    idade = int(input("Idade: "))
    renda = float(input("Renda mensal (R$): "))
    valor = float(input("Valor desejado do empréstimo (R$): "))
    parcelas = int(input("Número de parcelas (3 a 24): "))

    # Verifica se pode aprovar
    if pode_aprovar(idade, renda, valor, parcelas):
        valor_total = calcular_juros(valor, parcelas)
        valor_parcela = calcular_parcela(valor_total, parcelas)
        juros_totais = valor_total - valor

        # Exibição dos resultados
        print(f"\n✅ Empréstimo aprovado para {nome}!")
        print(f"📌 Valor total com juros: R$ {valor_total:.2f}")
        print(f"📆 Parcelado em {parcelas}x de R$ {valor_parcela:.2f}")
        print(f"💸 Juros totais pagos: R$ {juros_totais:.2f}")
    else:
        print(f"\n❌ Empréstimo negado para {nome}. Verifique os critérios de aprovação.")


if __name__ == "__main__":
    main()
