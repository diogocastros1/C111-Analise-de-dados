import numpy as np

# # NumPy Array
# # 1-D
# arr = np.array([1, 2, 3, 4])
# print(arr)
# print(type(arr))

# # 2-D
# mtz = np.array([[1,2],[3,4]])
# print(mtz)
# print(type(mtz))

# # ones 
# arr = np.ones(10)
# print(arr)

# # zeros
# arr = np.zeros(10)
# print(arr)

# # aranges
# arr = np.arange(20)
# print(arr)

# # aranges dois elementos
# arr = np.arange(20, 30)
# print(arr)

# # aranges dois f,l,s (inical, final e passo)
# arr = np.arange(20, 50, 5)
# print(arr)

# Operações entre NumPy Arrays
jan = np.arange(20, 30, 1)
fev = np.arange(40, 50, 1)
print(jan)
print(fev)
print(jan+fev)
print(np.concatenate([jan, fev]).reshape(5, 4))

# Tamanho de um array
print(jan.size)

# Dimensao
print(jan.ndim)

# Shape
print(jan.shape)
