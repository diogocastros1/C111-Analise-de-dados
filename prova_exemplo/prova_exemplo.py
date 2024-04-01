import numpy as np

arr = np.loadtxt('c:/Users/diogoantonio/Documents/codigos/C111-Analise-de-dados/prova_exemplo/paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# 1
print(arr[:,0:4])

# 2 
cont_paises = len(np.unique(arr[:,1]))
print(f'Total de paises: {cont_paises}')
print(f'Paises unicos: {np.unique(arr[:,1])}')

# 3 
med_alfabetizacao = arr[1:,9].astype(float).mean()
print(f'A media de alfabetizacao dos paises: {med_alfabetizacao:.2f}%')

# 4 
america_norte = np.char.find(arr[:,1], 'NORTHERN AMERICA')>=0
print(f'Paises da America do norte: {np.count_nonzero(america_norte)}')

# 5 
america_latina = np.char.find(arr[:,1], 'LATIN AMER. & CARIB')>=0
pais_maior_percapita = np.argmax(arr[america_latina, 8].astype(float))
max_percapita = np.max(arr[america_latina, 8].astype(float))

print(f"Pais {arr[:, 0][pais_maior_percapita]}possui a renda de ${max_percapita:.2f}")

