'''alunos = {'Ana':[],'João':[],'Maria':[]}
nomes = input('Digite o nome do aluno: ')
notas = float(input('Digite suas notas: '))

def cadastrar (a,b):
    if nomes in alunos:
        alunos[nomes].append(notas)
        return print(alunos)
cadastrar()'''


'''def media(a,b):
    return print(sum(a)/len(b))

def situacao(a):
    if a > 7:
        print('Voce esta aprovado')
    else:
        print('Voce esta de recuperação')'''

'''def boletim(a):
        print(alunos.items)'''

alunos = {'Ana':[],'João':[],'Maria':[]}
nomes = input('Digite o nome do aluno: ').title()

if nomes in alunos:
    for i in range(3):
        notas =float(input(f'Digite as notas {i+1} '))
        alunos[nomes].append(notas)
else:
    alunos[nomes] = []
    for i in range(3):
        notas =float(input(f'Digite as notas {i+1} '))
        alunos[nomes].append(notas)


print(alunos)




