print('BEM VINDO(A) A ESCOLHA DO LIDER DE TURMA ')

while True:
    try:
        nome = input('Digite seu nome: ').title()
        if not nome.isalpha():
            raise ValueError(('Digite um nome válido, sem números.'))
        
        else:
            break
    
    except ValueError as e:
        print(e)

while True:
    try:
        idade = int(input('Digite sua idade: '))
        if idade >= 14:
            break

        elif idade < 14:
            print('Você não pode votar, apenas maiores de 14 anos')        

    except ValueError:
        print('Digite Apenas números')

cand1 = 'João'
cand2 = 'Maria'
cand3 = 'Jose'

votos_cand1 = 0
votos_cand2 = 0
votos_cand3 = 0

while True:
    try:   
        opcao = (int(input(f'Em quem você deseja votar:\n1 - {cand1}\n2 - {cand2}\n3 - {cand3}:\n')))
        if opcao in [1,2,3]:
            if opcao == 1:
                votos_cand1 += 1
                votarnov = input('Você quer votar novamente? S/N:').upper()
                if votarnov == 'S':
                    print('Escolha seu proximo candidato')
                elif votarnov == 'N':
                    print('Obrigado por participar da votação!')
                    break
            elif opcao == 2:
                votos_cand2 += 1
                votarnov = input('Você quer votar novamente? S/N:').upper()
                if votarnov == 'S':
                    print('Escolha seu proximo candidato')
                elif votarnov == 'N':
                    print('Obrigado por participar da votação!')
                    break
            elif opcao == 3:
                votos_cand3 += 1
                votarnov = input('Você quer votar novamente? S/N:').upper()
                if votarnov == 'S':
                    print('Escolha seu proximo candidato')
                elif votarnov == 'N':
                    print('Obrigado por participar da votação!')
                    break
            print('Voto registrado com sucesso!')
        else:
            print('Digite apenas números válidos para candidatos!')
    except ValueError:
        print()
            

print(f'O candidato {cand1} teve {votos_cand1} votos!\nO candidato {cand2} teve {votos_cand2} votos!\n O candidato {cand3} teve {votos_cand3} votos! ')

while True:
    try:
        if votos_cand1 > votos_cand2 and votos_cand1 > votos_cand3:
            print(f'O {cand1} é o vencedor!')
            break
        elif votos_cand2 > votos_cand1 and votos_cand2 > votos_cand3:
            print(f'A {cand2} é a vencedora!')
            break
        elif votos_cand3 > votos_cand1 and votos_cand3 > votos_cand2:
            print(f'O {cand3} é o vencedor!')
            break
        elif votos_cand1 == votos_cand2 or votos_cand1 == votos_cand3 or votos_cand3 == votos_cand2:
            print('A Eleição deu empate!')
            break
    except ValueError:
        print()
