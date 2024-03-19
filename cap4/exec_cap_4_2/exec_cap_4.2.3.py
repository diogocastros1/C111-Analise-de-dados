'''
3. Mostre o resultado da média de cada linha e cada coluna da 
matriz gerada pela questão 2, e em seguida, apresente o maior 
valor das médias para as linhas e também para as colunas; 
'''
import numpy as np

np.random.seed(10)

# Criando um vetor com 16 numereos de 1 a 50
arr = np.random.randint(1, 51, 16)

# Transformando o vetor em uma matriz 4x4
mtz = arr.reshape(4,4)
print(mtz, '\n')

med_line = mtz.mean(axis=1)
med_col = mtz.mean(axis=0)
print(f'Media das linhas: {med_line}') 
print(f'Media das colunas: {med_col}') 