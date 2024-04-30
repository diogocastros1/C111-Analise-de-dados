import numpy as np

arr = np.loadtxt('C:/Users/diogoantonio/Documents/codigos/C111-Analise-de-dados/NP1/brands.csv', delimiter=';', dtype=str)

# 1
google = np.char.find(arr[:,0], 'Google')>=0
valoation = arr[google,9].astype(float) - arr[google,10].astype(float)

print(f'A Google valorizou ${valoation} de 2021 para 2022')

# 2
brands_group = np.char.find(arr[:,0], 'Group')>=0
print(f'Um total de {len(arr[brands_group,0])} marcas possuem Group em seu nome.')

# 3
brand_name = arr[1:6,0]
ten_percent = arr[1:6, 10].astype(float)*1.1
print(f'Os 5 primeiros paises são {brand_name} e o valor se o aumento tivesse sido de 10%, estes seriam seus respectivos valores {ten_percent}')

# 4
info_brand = arr[1:,0:2]
founded = arr[1:,2].astype(int)>=2000
print(info_brand[founded])

# 5
year_founded = np.unique(arr[1:,2].astype(int))
print(f'Estes são todos os anos em que empresas foram fundadas: {year_founded}')

year_more_founded = len(np.unique(arr[1:,2].astype(int)))

print(f'O ano que teve mais empresas fundadas foi {arr[year_more_founded,2]} com {year_more_founded} empresas')

