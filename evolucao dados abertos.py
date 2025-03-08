import matplotlib.pyplot as plt

# Dados de anos e percentuais
anos = [2023, 2024, 2025]
percentuais = [14.8, 22.2, 40.7]

# Criando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(anos, percentuais, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)

# Adicionando títulos e rótulos
plt.title('Evolução da Disponibilização de Dados Abertos', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Percentual de Disponibilização (%)', fontsize=12)

# Exibindo o gráfico
plt.grid(True)
plt.xticks(anos)
plt.yticks(range(0, 101, 10))
plt.show()
