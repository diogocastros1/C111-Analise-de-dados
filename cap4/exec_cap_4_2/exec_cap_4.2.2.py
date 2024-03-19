'''
2. Crie uma matriz de tamanho 4x4 formada por números 
aleatórios inteiros entre 1 e 50; (use seed(10) antes)
'''

import numpy as np

np.random.seed(10)

# Criando um vetor com 16 numereos de 1 a 50
arr = np.random.randint(1, 51, 16)
print(arr, '\n')

# Transformando o vetor em uma matriz 4x4
mtz = arr.reshape(4,4)
print(mtz)