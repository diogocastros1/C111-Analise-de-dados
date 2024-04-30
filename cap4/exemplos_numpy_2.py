import numpy as np

# Numeros aleatorios 
# Random
arr = np.random.randint(1, 11, 15)
print(arr)

# SEED -> semente aleatoria
np.random.seed(10)
arr = np.random.randint(1, 11, 15)
print(arr)

# Extraindo elementos unicos
# print(np.unique(arr, return_counts=True))

# Operações com matrizes
mtz = arr.reshape(3,5)
print(mtz)

'''  J   F  M  A  J
agua 10  5  1  2 10
luz   1  2  9 10  1
Net   9  7  5  4  1
'''
# Retornando a soma dos gastos com agua
# print(f'Gastos com agua {mtz.sum(axis=1)[0]}') # contando a linha 1
# print(f'Gastos de janeiro {mtz.sum(axis=0)[0]}') # contando a coluna 1

# Broadcasting
# Multiplicando a matriz por 0.5
# print(0.5*mtz)

# Condicionais 
cond = mtz%2==0 # pegando os elementos pares
# print(cond)
# print(mtz[cond])

cond2 = mtz>mtz.mean() # extraindo valores mariores que a média
# print(cond2)
# print(mtz[cond2])

# Analise textual
# CHAR
arr = np.array(['Pedro', 'Arthur', 'Ana', 'Maciel'])
result = np.char.find(arr, 'An')>=0
cond = np.char.find(arr, 'a') >= 0
print(result)
print(arr[result])
print(cond)
print(arr[cond])