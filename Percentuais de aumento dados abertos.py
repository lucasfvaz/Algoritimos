import matplotlib.pyplot as plt

# Dados de anos e percentuais
anos = [2023, 2024, 2025]
percentuais = [14.8, 22.2, 40.7]

# Cálculo dos aumentos percentuais
aumento_2023_2024 = ((percentuais[1] - percentuais[0]) / percentuais[0]) * 100
aumento_2024_2025 = ((percentuais[2] - percentuais[1]) / percentuais[1]) * 100

# Criando o gráfico de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(anos, percentuais, color='skyblue', width=0.5)

# Adicionando títulos e rótulos
plt.title('Taxa de aumento da Disponibilização de Dados Abertos', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Percentual de Disponibilização (%)', fontsize=12)

# Adicionando anotações mais para cima das barras com mais estilo
plt.text(2024, percentuais[1] + 4, f'Aumento: {aumento_2023_2024:.2f}%', 
         ha='center', fontsize=14, color='white', fontweight='bold',
         bbox=dict(facecolor='red', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.3'))

plt.text(2025, percentuais[2] + 4, f'Aumento: {aumento_2024_2025:.2f}%', 
         ha='center', fontsize=14, color='white', fontweight='bold',
         bbox=dict(facecolor='green', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.3'))

# Exibindo o gráfico
plt.xticks(anos)
plt.yticks(range(0, 101, 10))
plt.grid(True)
plt.show()
