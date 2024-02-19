# C111 Analise de dados

## Cap 3 - Coleções
Coleções são um conjunto de coisas.
- Slicing -> Fatiar as coleções.

### Tuplas (Tuples)
Tuplas são contidas por parenteses ().
- Tuplas são imutaveis, portanto após cria-las não será possivel efetuar nenhuma atualização.
~~~python
nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
# Slicing de dados
print(nomes[0])
print(nomes[:2]) # premeiro argumento é inlusive e o segundo exclusive
print(nomes[1:3]) # de 1 a 2
print(nomes[-2]) # busca de tras pra frente
# Update não funciona
~~~

### Listas (Lists)
São contidas por colchetes [].
~~~python
# nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
# Add
nomes.append('Bulma')
# Update
nomes[0] = 'Goten'
# Delete
nomes.remove('Trunks') # Remocao por valor
del nomes[2] # Remocao por indice
# Select
print(nomes)
~~~

### Conjunto (Set)
São contidas por chaves {}.
- Não guardam as ordens dos elementos.
- Não guarda elementos repetidos.
- Para remover itens duplicados de uma lista, podemos transforma-la em um conjunto, porém este metodo deve ser utilizado somente para poucos dados, pois como se trata de um recurso nativo do python, consome um certo processamento.
~~~python
nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}
# Add
nomes.add('Bulma')
nomes.add('Goku')
print(nomes)
# Remove
nomes.remove('Gohan')
# Update não funciona
~~~

### Dicionarios (Dictionary)
O JSON do Python, estrutura de chave e valor.
~~~python
pessoa = {'nome': 'Goku', 'idade': 42}
# Add 
pessoa['sexo'] = 'M'
# Delete
del pessoa['idade']
# Select
print(pessoa)
~~~

### Coleções Aninhadas
Uma coleção dentro de outra coleção.
~~~python
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
~~~

