import numpy as np

# Criando o array de números pares de 0 a 51
array1 = np.arange(0, 52, 2)

# Criando o array de números pares de 100 a 50
array2 = np.arange(100, 49, -2)

# Concatenando os arrays
concatenated_array = np.concatenate((array1, array2))

print("Array 1 de números pares de 0 a 51:")
print(array1)

print("\nArray 2 de números pares de 100 a 50:")
print(array2)

print("\nArray concatenado:")
print(concatenated_array)
