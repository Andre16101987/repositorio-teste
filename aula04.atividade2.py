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

cand1 = Goku
cand2 = Naruto
cand3 = Luffy

votos1 = 0
votos2 = 0
votos3 = 0

while True:
    try:
        opcao = int(input('\n1- Goku\n2- Naruto\n3- Luffy\n qual candidato voce escolhe: '))
        if opcao in [1,2,3]:
    match case:
        case 1:
            print("Voce escolheu o Goku")
            votos1 += 1:
        case 2:
            print('Voce escolheu Naruto')
        case 3:
            print('Voce escolheu Luffy')
        case _:
            print('Opção inválida')
           
        if opcao == 1:
        votos1 + 1
        opcao2 = input('Deseja votar novamente? S/N').upper()
        if opcao2 == 'S':
    match case:
        case 1:
            print("Voce escolheu o Goku")
        case 2:
            print('Voce escolheu Naruto')
        case 3:
            print('Voce escolheu Luffy')
        case _:
            print('Opção inválida')
            break
    except ValueError:
        print('Digite um número válido')




