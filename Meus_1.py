# [PY-A03] Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.

# O programa deve fornecer as seguintes funcionalidades:

# Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.

# Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.

# Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.

# O programa deve ser executado em um loop contínuo até que o usuário escolha sair.

dic = {}

while True:
    print('1 - Para adicionar um aluno')
    print('2 - Para remover um aluno')
    print('3 - Sair')

    cond = int(input('Agora me diga o que você deseja fazer: '))

    if cond == 1:
        matricula = input('Número da matrícula: ')
        nome_aluno = input('Nome do aluno: ')
        dic[matricula] = nome_aluno
    elif cond == 2:
        matricula_remover = input('Número da matrícula do aluno a ser removido: ')
        if matricula_remover in dic:
            del dic[matricula_remover]
        else:
            print('Matrícula não encontrada.')

    elif cond == 3:
        break

print("Alunos no dicionário:")
for matricula, nome_aluno in dic.items():
    print(f"Matrícula: {matricula}, Aluno: {nome_aluno}")

        
