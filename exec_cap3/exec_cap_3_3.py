
def salvar_alunos():
    dados_alunos = {}
    # Solicitar o número de alunos
    num_alunos = int(input('Quantos alunos deseja cadastrar? '))

    # Loop para solicitar os dados de cada aluno
    for i in range(num_alunos):
        nome_aluno = input(f'Digite o nome do aluno {i+1}: ')
        media_aluno = float(input(f'Digite a média do aluno {i+1}: '))
        
        # Verificar se o aluno está aprovado ou reprovado
        if media_aluno >= 60:
            situacao = 'AP'
        else:
            situacao = 'RP'
        
        # Adicionar os dados do aluno (incluindo a situação) ao dicionário
        dados_alunos[nome_aluno] = {'media': media_aluno, 'situacao': situacao}

    # Retornar o dicionário com os dados dos alunos
    return dados_alunos

# Chamar a função para salvar os dados dos alunos
dados_dos_alunos = salvar_alunos()
print('Dados dos alunos:')
for nome, dados  in dados_dos_alunos.items():
    print(f'Nome: {nome}, \n Media: {dados['media']}, \n Situacao: {dados['situacao']}')