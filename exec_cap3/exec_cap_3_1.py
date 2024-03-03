# Lista com 5 primeiros colocados
champs = ['Flamengo', 'Barcelona', 'Real Madrid', 'Bayern de Munique', 'Manchester City']

# Exibir os três primeiros colocados
print("Os tres primeiros colocados sao:")
for colocacao in champs[:3]:
    print(colocacao)
print('\n')
# Exibir os três primeiros colocados
print("Os dois ultimos colocados sao:")
for colocacao in champs[3:]:
    print(colocacao)

# Odenando a lista
champs_alfabetica = champs.copy()
champs_alfabetica.sort()
print(champs_alfabetica)

# Verificando a posição do barcelona
posicao_barcelona = champs.index('Real Madrid')
print(f'Barcelona esta na {posicao_barcelona}')
