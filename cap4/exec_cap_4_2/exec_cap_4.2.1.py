'''
1. Crie um array de floats com 10 elementos positivos e 
negativos entre 0 e 1. Em seguida, multiplique seus valores 
por 100 e crie um novo vetor apenas com a parte inteira 
destes números; (use seed(5) antes) 

'''
import numpy as np

np.random.seed(5)

# Criando um vetor com numeros aleatorios de 0 à 1 positivos ou negativos
arr = np.random.rand(10) * 2 - 1

# Multiplicando por 100
new_arr = arr * 100

# Extraindo somente a parte inteira dos numeros
arr_int = new_arr.astype(int)

print(arr_int)