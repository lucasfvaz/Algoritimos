import pandas as pd

# Cria um conjunto de dados
dados = {
    'Estado': [
        'Santa Catarina', 'Mato Grosso', 'Rondônia', 'Paraná', 
        'Rio Grande do Sul', 'Goiás', 'Minas Gerais', 
        'Mato Grosso do Sul', 'Tocantins', 'Espírito Santo',
        'Alagoas', 'Bahia', 'Amapá', 'Maranhão', 'Pernambuco', 
        'Pará', 'São Paulo',        'Sergipe', 'Acre', 'Amazonas', 
        'Ceará', 'Brasil', 'Roraima', 'Rio Grande do Norte', 
        'Rio de Janeiro', 'Distrito Federal', 'Piauí', 'Paraíba'
    ],
    'Ano_2023': [
        0.418, 0.452, 0.455, 0.463, 0.466, 0.473, 0.476, 0.477,
        0.477, 0.486, 0.486, 0.49, 0.491, 0.492, 0.496, 0.501, 
        0.504, 0.507, 0.511, 0.512, 0.513, 0.518, 0.52, 0.535, 
        0.54, 0.543, 0.552, 0.559
    ]
}

# Cria o DataFrame
df = pd.DataFrame(dados)

# Define as regiões
regioes = {
    'Norte': ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 
              'Roraima', 'Tocantins'],
    'Nordeste': [
        'Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 
        'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'
    ],
    'Sudeste': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 
                'São Paulo'],
    'Sul': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina'],
    'Centro-Oeste': ['Distrito Federal', 'Goiás', 'Mato Grosso', 
                     'Mato Grosso do Sul']
}

# Calcula a média por região no ano de 2023
medias = {}
for regiao, estados in regioes.items():
    medias[regiao] = df[df['Estado'].isin(estados)]['Ano_2023'].mean()

# Exibe as médias por região
for regiao, media in medias.items():
    print(f"Média do índice GINI em 2023 na região {regiao}: {media:.4f}")
