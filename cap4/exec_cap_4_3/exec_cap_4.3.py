import numpy as np

arr = np.loadtxt('c:/Users/diogoantonio/Documents/codigos/C111-Analise-de-dados/cap4/exec_cap_4_3/space.csv', delimiter=';', dtype=str, encoding='utf-8')

# 1. Extraindo um percentual das missões que tem o status de sucesso
status_sucesso = arr[:, 7] == 'Success'
porcentagem_sucesso = np.sum(status_sucesso) / len(status_sucesso) * 100
print(f'{porcentagem_sucesso:.2f}% das missoes foram bem sucedidas')

# 2. Qual a media de gastos de uma missao, baseando em missoes que possuem valores disponiveis
gastos_disponiveis = arr[1:, 6].astype(float)
gastos_disponiveis = gastos_disponiveis[~np.isnan(gastos_disponiveis)]
media_gastos = np.mean(gastos_disponiveis)
print(f'A media de gastos de uma missao e de ${media_gastos:.2f}M')


# 3. Quantidade de missoes realizadas pelo Estados Unidos
pais_estados_unidos = np.char.find(arr[1:,2], 'USA')>=0
quantidade_estados_unidos = np.count_nonzero(pais_estados_unidos)
print(f'Foram realizadas {quantidade_estados_unidos} missoes pelo Estados Unidos')

# 4. A missao mais cara realizada pela SpaceX
spacex = np.char.find(arr[:,1], 'SpaceX')>=0
spacex_max = np.max(arr[spacex,6].astype(float))
print(f'A missao mais cara da SpaceX custou ${spacex_max:.2f}M.')

# 5. Empresas que realizaram missoes com as respsctivas quantidade de missoes
empresas_contagem = np.unique(arr[1:,1], return_counts=True)
empresas_contagem = dict(zip(empresas_contagem[0], empresas_contagem[1]))
print('As empresas que realizaram missoes com a respectiva quantidade de missoes sao:')
for empresa, qtd in empresas_contagem.items():
  print(f'{empresa}: {qtd}')

