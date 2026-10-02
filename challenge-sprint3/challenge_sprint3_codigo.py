# Challenge Sprint 3 - Análises Estatísticas e Regressão Linear
# Trabalho em grupo - 1CCPW
# Ryan Amorim De Castro Santana - RM:564393

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1) Carregar base de dados
file_path = "base_dados_goodwe_ficticia.xlsx"
df = pd.read_excel(file_path)

# Selecionando variável aleatória para análise
variavel = "Potência (W)"  # Exemplo de variável numérica
dados = df[variavel].dropna()

# --------------------------------------------------------------------
# Questão 01 - Probabilidade acima da mediana
mediana = np.median(dados)
media = np.mean(dados)
desvio = np.std(dados, ddof=1)

# Probabilidade de estar acima da mediana em uma Normal
prob_acima_mediana = 1 - norm.cdf(mediana, loc=media, scale=desvio)

print("Questão 01 - Probabilidade acima da mediana")
print(f"Mediana = {mediana:.2f}")
print(f"Probabilidade acima da mediana = {prob_acima_mediana:.4f}")

# --------------------------------------------------------------------
# Questão 02 - Probabilidade dentro do intervalo (média ± 2s)
lim_inf = media - 2*desvio
lim_sup = media + 2*desvio

prob_intervalo = norm.cdf(lim_sup, loc=media, scale=desvio) - norm.cdf(lim_inf, loc=media, scale=desvio)

print("\nQuestão 02 - Probabilidade dentro do intervalo (média ± 2s)")
print(f"Média = {media:.2f}, Desvio padrão = {desvio:.2f}")
print(f"Intervalo = ({lim_inf:.2f}, {lim_sup:.2f})")
print(f"Probabilidade = {prob_intervalo:.4f}")

# --------------------------------------------------------------------
# Questão 03 - Regressão Linear
# Exemplo: relação entre 'Potência (W)' e 'Energia (kWh)'
X = df[['Potência (W)']].dropna()
y = df.loc[X.index, 'Energia (kWh)']

modelo = LinearRegression()
modelo.fit(X, y)

coef_angular = modelo.coef_[0]
intercepto = modelo.intercept_

print("\nQuestão 03 - Regressão Linear")
print(f"Coeficiente angular (beta1) = {coef_angular:.4f}")
print(f"Intercepto (beta0) = {intercepto:.4f}")

