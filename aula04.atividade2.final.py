print('Bem vindo as eleições de representante')

while True:
    try:
        votante = input('Digite seu nome')
        if not votante.isalpha():
            raise ValueError('Digite um nome válido')
        break
    except ValueError as e:
        print(e)

while True:
    try:
        idade = int(input(" digite sua idade"))
        if idade >= 14:
            break
        else:
            print('Infelimente voce não tem a idade correta')
    except ValueError:
        print('Digite um numero')

cand1 = 'Goku'
cand2 = 'Naruto'
cand3 = 'Luffy'

votos1 = 0
votos2 = 0
votos3 = 0

while True:
    try:
        opcao = int(input('\n1- Goku\n2- Naruto\n3- Luffy\n qual candidato voce escolhe: '))
        if opcao in [1,2,3]:
            
            match opcao:
                case 1:
                    print("Voce escolheu o Goku")
                    votos1 += 1
                    votnov = input('Vc quer continuar votando? S/N').upper()
                    if votnov == 'S':
                        print('Escolha o próximo candidato')
                    elif votnov == 'N':
                        print('Obrigado por votar')
                        break
                case 2:
                    print('Voce escolheu Naruto')
                    votos2 += 1
                    votnov = input('Vc quer continuar votando? S/N').upper()
                    if votnov == 'S':
                        print('Escolha o próximo candidato')
                    elif votnov == 'N':
                        print('Obrigado por votar')
                        break
                case 3:
                    print('Voce escolheu Luffy')
                    votos3 += 1
                    votnov = input('Vc quer continuar votando? S/N').upper()
                    if votnov == 'S':
                        print('Escolha o próximo candidato')
                    elif votnov == 'N':
                        print('Obrigado por votar')
                        break
        else:
            print('Opção inválida')
    except ValueError:
        print('Digite um número válido')

print(f'O candidato {cand1} teve {votos1} votos!\nO candidato {cand2} teve {votos2} votos!\n O candidato {cand3} teve {votos3} votos! ')

while True:
    try:
        if votos1 > votos2 and votos1 > votos3:
            print(f'O {cand1} é o vencedor!')
            break
        elif votos2 > votos1 and votos2 > votos3:
            print(f'A {cand2} é a vencedora!')
            break
        elif votos3 > votos1 and votos3 > votos2:
            print(f'O {cand3} é o vencedor!')
            break
        elif votos1 == votos2 or votos1 == votos3 or votos3 == votos2:
            print('A Eleição deu empate!')
            break
    except ValueError:
        print()




