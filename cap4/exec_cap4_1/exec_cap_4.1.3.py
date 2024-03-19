import numpy as np

# Criando o array de números pares de 0 a 51
array1 = np.arange(0, 52, 2)

# Criando o array de números pares de 100 a 50
array2 = np.arange(100, 49, -2)

# Ordenando os arrays
array1_sorted = np.sort(array1)
array2_sorted = np.sort(array2)

# Concatenando os arrays ordenados
concatenated_array = np.concatenate((array1_sorted, array2_sorted))

print("Array 1 de números pares de 0 a 51:")
print(array1_sorted)

print("\nArray 2 de números pares de 100 a 50:")
print(array2_sorted)

print("\nArray concatenado e ordenado:")
print(concatenated_array)
