import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
data = {
    "Regiao": ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"],
    "taxa_homicidios": [34, 36.5, 22.6, 14, 16.4],
    "risco_relativo": [4.773290, 5.202604, 3.640565, 3.506040, 3.410589],
}
df = pd.DataFrame(data)

# Gráfico 1: Taxa de Homicídios por Município
plt.figure(figsize=(10, 6))
plt.bar(df["Regiao"], df["taxa_homicidios"], color="coral", edgecolor="black")
plt.xlabel("Regiões", fontsize=12)
plt.ylabel("Taxa de Homicídios", fontsize=12)
plt.title("Taxa de Homicídios por Regiao", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfico 2: Risco Relativo por Município
plt.figure(figsize=(10, 6))
plt.bar(df["Regiao"], df["risco_relativo"], color="lightgreen", edgecolor="black")
plt.xlabel("Regiões", fontsize=12)
plt.ylabel("Risco Relativo", fontsize=12)
plt.title("Risco Relativo por Regiao", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfico 3: Comparação entre Taxa de Homicídios e Risco Relativo (Gráfico de Linhas)
plt.figure(figsize=(10, 6))
plt.plot(df["Regiao"], df["taxa_homicidios"], marker="o", label="Taxa de Homicídios", color="blue")
plt.plot(df["Regiao"], df["risco_relativo"], marker="s", label="Risco Relativo", color="green")
plt.xlabel("Regiões", fontsize=12)
plt.ylabel("Valores", fontsize=12)
plt.title("Comparação entre Taxa de Homicídios e Risco Relativo", fontsize=14)
plt.legend(fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfico 4: Comparação do Risco Relativo entre Municípios (Novo Gráfico)
plt.figure(figsize=(10, 6))
plt.bar(df["municipio"], df["risco_relativo"], color="skyblue", edgecolor="black")
plt.xlabel("Regiões", fontsize=12)
plt.ylabel("Risco Relativo", fontsize=12)
plt.title("Comparação do Risco Relativo entre Regiões", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
