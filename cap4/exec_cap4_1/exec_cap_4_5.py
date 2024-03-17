import numpy as np

# Definindo o tamanho da matriz
num_linhas = 5
num_colunas = 4

# Criando a matriz de tamanho especificado
matriz = np.zeros((num_linhas, num_colunas))  # Pode ser zeros, uns ou qualquer valor desejado

# Extraindo o número de linhas e colunas
total_linhas, total_colunas = matriz.shape

# Calculando o tamanho total da matriz
tamanho_total = total_linhas * total_colunas

# Verificando se o tamanho total é par ou ímpar
if tamanho_total % 2 == 0:
    print("O número de elementos da matriz é par.")
else:
    print("O número de elementos da matriz é ímpar.")
