import pandas as pd

file_path = r'C:\Users\lucas\Downloads\data.xlsx'

# Abrir o arquivo Excel
data = pd.ExcelFile(file_path)

# Lê a planilha 
sheet_data = data.parse('Worksheet')

# Faz o Mapeamento de estados para suas respectivas regiões
region_mapping = {
    'Norte': ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 
              'Tocantins'],
    'Nordeste': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 
                 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
    'Centro-Oeste': ['Distrito Federal', 'Goiás', 'Mato Grosso', 
                     'Mato Grosso do Sul'],
    'Sudeste': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 
                'São Paulo'],
    'Sul': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
}

# Adiciona uma nova coluna para a região correspondente
def assign_region(state):
    for region, states in region_mapping.items():
        if state in states:
            return region
    return None

sheet_data['Região'] = sheet_data['Territorialidade'].apply(assign_region)

# Calcula a média de IDH por região
average_idh_by_region = sheet_data.groupby('Região')['IDHM'].mean()

# Exibe os resultados
print(average_idh_by_region)