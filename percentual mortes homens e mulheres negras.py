import matplotlib.pyplot as plt

# Dados
total_homens = 42527
homens_negros = 32993
homens_nao_negros = total_homens - homens_negros

total_mulheres = 3806
mulheres_negras = 2526
mulheres_nao_negras = total_mulheres - mulheres_negras

# Gráfico 1: Percentual de homens negros
plt.figure(figsize=(10, 5))

# Homens negros e não negros
plt.subplot(1, 2, 1)
plt.pie(
    [homens_negros, homens_nao_negros],
    labels=["Homens Negros", "Homens Não Negros"],
    autopct='%1.1f%%',
    startangle=90,
    colors=["red", "orange"],
    explode=(0.1, 0)
)
plt.title("Percentual de Homens Negros")

# Gráfico 2: Percentual de mulheres negras
plt.subplot(1, 2, 2)
plt.pie(
    [mulheres_negras, mulheres_nao_negras],
    labels=["Mulheres Negras", "Mulheres Não Negras"],
    autopct='%1.1f%%',
    startangle=90,
    colors=["purple", "pink"],
    explode=(0.1, 0)
)
plt.title("Percentual de Mulheres Negras")

# Exibir os gráficos
plt.tight_layout()
plt.show()
