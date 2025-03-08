import pandas as pd
import matplotlib.pyplot as plt

# Dados fornecidos
dados = {
    "Ano": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "MVI_Brasil": [55844, 59739, 58437, 61600, 64079, 57592, 47765, 50448, 48286, 47963, 46328]
}

# Criação do DataFrame
df = pd.DataFrame(dados)

# Cálculo da redução percentual
pico = df["MVI_Brasil"].max()
valor_2023 = df.loc[df["Ano"] == 2023, "MVI_Brasil"].values[0]
reducao_percentual = ((pico - valor_2023) / pico) * 100

# # Gráfico de evolução
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.plot(df["Ano"], df["MVI_Brasil"], marker='o', linestyle='-', color='b', label='MVI - Brasil')
# plt.title('Evolução das Mortes Violentas Intencionais (2013-2023)', fontsize=12)
# plt.xlabel('Ano', fontsize=10)
# plt.ylabel('Nº de Mortes', fontsize=10)
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
# plt.xticks(df["Ano"], rotation=45)

# Gráfico de redução percentual
plt.subplot(1, 2, 2)
plt.bar(['Redução de 2017 a 2023'], [reducao_percentual], color='orange', alpha=0.8)
#plt.title('Redução Percentual de MVI (2017-2023)', fontsize=12)
plt.ylabel('Redução (%)', fontsize=10)
#plt.ylim(0, 30)
plt.text(0, reducao_percentual / 2, f'{reducao_percentual:.1f}%', ha='center', fontsize=12, color='black')

plt.tight_layout()
plt.show()
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Exemplo de dados fictícios
# Dados municipais de homicídios e variáveis explicativas
data = {
    "municipio": ["A", "B", "C", "D", "E"],
    "homicidios": [25, 40, 35, 50, 30],
    "idh_m": [0.65, 0.70, 0.60, 0.75, 0.68],
    "gini": [0.45, 0.50, 0.48, 0.47, 0.46],
    "urbanizacao": [0.85, 0.90, 0.80, 0.95, 0.88],
    "populacao": [50000, 70000, 40000, 100000, 60000]
}

# Convertendo para um DataFrame
df = pd.DataFrame(data)

# Calculando a variável de risco relativo (ri,t)
# Normalizamos homicídios pela população (taxa por 100 mil habitantes)
df["taxa_homicidios"] = (df["homicidios"] / df["populacao"]) * 100000

# Definindo as variáveis explicativas (X) e a variável dependente (y)
X = df[["idh_m", "gini", "urbanizacao", "populacao"]]
y = np.log(df["taxa_homicidios"])  # Log-transformada da taxa de homicídios

# Adicionando uma constante para o termo alfa (intercepto)
X = sm.add_constant(X)

# Ajustando o modelo de regressão
model = sm.OLS(y, X).fit()

# Exibindo o resumo do modelo
print(model.summary())

# Prevendo o risco relativo (ri,t) para os municípios
df["risco_relativo"] = model.predict(X)

# Exibindo os resultados
print("\nResultados:")
print(df[["municipio", "taxa_homicidios", "risco_relativo"]])
