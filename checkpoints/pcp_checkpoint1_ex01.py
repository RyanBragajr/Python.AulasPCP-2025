# Entrada
valor_real = int(input("Digite o valor do real ?"))

# Coversão de moedas (valores aproximados 10/04 pelo site da 'Wize')

dolar = 5.92

euro = 6.62

peso_arg = 0.01

libra = 7.67

iene = 0.04

# Conversões
valor_dolar = valor_real / dolar

valor_euro = valor_real / euro

valor_peso = valor_real / peso_arg

valor_libra = valor_real / libra

valor_iene = valor_real / iene

# Resultado com 2 casas decimais que prof pediu
print(f"\nValor em Real: R$ {valor_real:.2f}")
print(f"Valor em Dólar: US$ {valor_dolar:.2f}")
print(f"Valor em Euro: € {valor_euro:.2f}")
print(f"Valor em Peso Argentino: ARS$ {valor_peso:.2f}")
print(f"Valor em Libra Esterlina: £ {valor_libra:.2f}")
print(f"Valor em Iene: ¥ {valor_iene:.2f}")