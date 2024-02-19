# Coleções 
# Tuplas -> são contidas por paranteses ()
# nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')

# # Slicing de dados
# print(nomes[0])
# print(nomes[:2]) # premeiro argumento é inlusive e o segundo exclusive
# print(nomes[1:3]) # de 1 a 2
# print(nomes[-2]) # busca de tras pra frente
# Update não funciona

# Listas
# nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
# # Add
# nomes.append('Bulma')
# # Update
# nomes[0] = 'Goten'
# # Delete
# nomes.remove('Trunks') # Remocao por valor
# del nomes[2] # Remocao por indice
# # Select
# print(nomes)

# Conjuntos
# nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}
# # Add
# nomes.add('Bulma')
# nomes.add('Goku')
# print(nomes)
# # Remove
# nomes.remove('Gohan')
# # Update não funciona

# Dicionario
pessoa = {'nome': 'Goku', 'idade': 42}
# Add 
pessoa['sexo'] = 'M'
# Delete
del pessoa['idade']
pessoa2 = {'nome': 'Bulma', 'idade': 40}
# Add 
pessoa2['sexo'] = 'M'
# Delete
del pessoa2['idade']
# Select
print(pessoa)

# Colecoes aninhadas
nomes = [pessoa, pessoa2]
print(nomes[1]['nome']) # acessando o nome da Bulma

