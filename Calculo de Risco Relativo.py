import numpy as np
import pandas as pd
import statsmodels.api as sm

# Dados regionais de homicídios e variáveis explicativas
data = {
    "regiao": ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"],
    "homicidios": [5.892, 19.967, 3.682, 11.889, 4.898],
    "idh_m": [0.683, 0.659, 0.753, 0.753, 0.756],
    "gini": [0.495, 0.514, 0.486, 0.501, 0.449],
    "urbanizacao": [78.47, 77.64, 91.35, 94.44, 88.24],  
    "populacao": [17.349619, 54.644582, 16.287809, 84.847187, 29.933315]
}

# Criando DataFrame
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

# Prevendo o risco relativo (ri,t) para as regiões
df["risco"] = model.predict(X)

df["risco_relativo"] = (
    df["risco"] * (1 - df["idh_m"])  # Maior IDH reduz o risco
    * (1 + 0.5 * df["gini"])                 # Maior GINI aumenta o risco
    * (1 + 0.2 * df["urbanizacao"] / 100)    # Maior urbanização aumenta o risco um pouco
)

# Exibindo os resultados finais
print("\nResultados ajustados:")
print(df[["regiao", "risco_relativo"]])
