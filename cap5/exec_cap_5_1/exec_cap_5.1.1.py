import numpy as np
import pandas as pd

# Lendo arquivo
df = pd.read_csv('c:/Users/diogoantonio/Documents/codigos/C111-Analise-de-dados/cap5/paises.csv', delimiter=';')

# 1 a) 
oceania = df.loc[df['Region'].str.contains('OCEANIA'), 'Country']
print(oceania)

# 1 b)
print(f'Total de paise da Oceania: {oceania.count()}')

# 2
literacy = df['Literacy (%)']
print(f'Media de alfabetizacao mundial eh: {literacy.mean():.2f}%')

# 3
max_pop = df['Population'].max()
pais = df.loc[df['Population'] == max_pop, 'Country'].to_string(index=False).strip()
region_pais = df.loc[df['Population'] == max_pop, 'Region'].to_string(index=False).strip()
print(f'O pais com maior populacao eh a {pais}, que fica na regiao da {region_pais} e possui uma populacao de {'{:,}'.format(max_pop).replace(',', '.')}')

# 4
no_coastline = df.loc[df['Coastline (coast/area ratio)'] <= 0, 'Country']
print(no_coastline)

# 5
no_coastline = df.loc[df['Coastline (coast/area ratio)'] <= 0, 'Country']
print(no_coastline)
no_coastline.to_csv('c:/Users/diogoantonio/Documents/codigos/C111-Analise-de-dados/cap5/exec_cap_5_1/no_coastline.csv', index=False)