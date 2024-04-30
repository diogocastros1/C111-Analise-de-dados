import numpy as np
import pandas as pd

# SERIES (1-D)
dic = {'a':10, 'b':20, 'c':30}
series1 = pd.Series(dic)
print(series1)

series2 = pd.Series(data=[20, 30, 40], 
                    index=['b', 'c', 'd'])

# somando os valores das duas series
print(series1+series2)

print(series1.add(series2))

# Somando, porem adicionando os valores ausentes como 0
print(series1.add(series2, fill_value=0))

print(series1['a'])

# Para acessar múltiplos valores precisamos adicionar um par de colchetes a mais, pois se trata de uma lista de elementos
print(series1[['b', 'c']])

# Condicionais
print(series1[series1>10])

# DATAFRAMES (2-D)
df = pd.DataFrame(
  columns = ['X', 'Y', 'Z'],
  index = ['A', 'B', 'C'],
  data= np.random.randint(1, 50, [3,3])
)
print(df)

# Slicing de um DataFrame
# .loc -> Localiza pelo indice customizado
# .iloc -> Localiza pelo indice indefinido

print(df.loc['B':,'X':'Z'])
print(df.iloc[1:, :])

# Ler um dataset no pandas
df = pd.read_csv('c:/Users/diogoantonio/Documents/codigos/C111-Analise-de-dados/cap5/paises.csv', delimiter=';')
print(df)

# Colunas do dataset
print(df.columns)

# Somente os nomes dos paises
print(df['Country'])

# Somente os 3 primeiros
print(100*'\n')
print(df.head(3))

# Somente os 3 ultimos
print(100*'\n')
print(df.tail(3))