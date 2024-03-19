'''
4. Baseado na matriz gerada na questão 2, mostre a 
quantidade de aparições de cada um dos números na mesma. 
Em seguida, mostre apenas os números que aparecem 2 vezes. 
'''
import numpy as np

np.random.seed(10)

# Criando um vetor com 16 numereos de 1 a 50
arr = np.random.randint(1, 51, 16)

# Transformando o vetor em uma matriz 4x4
mtz = arr.reshape(4,4)
print(mtz)

print(np.unique(mtz, return_counts=True))

# Encontra os valores únicos e as contagens de cada valor
nums, counts = np.unique(mtz, return_counts=True)

# Encontra os números que aparecem duas vezes
numeros_repetidos = nums[counts == 2]

print("\nNúmeros que aparecem duas vezes na matriz:")
print(numeros_repetidos)