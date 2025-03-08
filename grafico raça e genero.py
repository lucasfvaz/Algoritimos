import matplotlib.pyplot as plt

# Dados
categorias = [
    "Total de Mortes", 
    "Homens", 
    "Homens Negros", 
    "Homens Não Negros", 
    "Mulheres", 
    "Mulheres Negras", 
    "Mulheres Não Negras"
]
valores = [46409, 42527, 32993, 8976, 3806, 2526, 1227]

# Configurando o gráfico
plt.figure(figsize=(10, 6))
plt.bar(categorias, valores, color=['blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink'])
plt.title("Distribuição de Mortes por Gênero e Cor no Brasil", fontsize=14)
plt.ylabel("Número de Mortes", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibindo o gráfico
plt.tight_layout()
plt.show()
  