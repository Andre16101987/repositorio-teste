print('Seja bem vindo ao Senac')

while True:
    try:
        nome = input('Digite seu nome')
        if not nome.isalpha():
            raise ValueError('Digite um nome válido')
        break
    except ValueError as e:
        print(e)
while True:
    try:
        escolaridade = input('Digite sua escolaridade')
        if not nome.isalpha():
            raise ValueError('Digite um nome válido')
        break
    except ValueError as e:
        print(e)
        
while True:
    try:
        cpf = int(input('Digite seu cpf'))
        break
    except ValueError:
            print('Digite um numero')
        
while True:
    try:
        opcao = int(input('\n1- análise de dados\n2- power bi\n3- desenvolvimento de banco de dados\n4- outro\n qual curso voce deseja fazer conosco: '))
        if opcao in [1,2,3,4]:
            break
    except ValueError:
        print('Digite um numero')
            
match case:
    case 1:
        print(f'Parabéns {nome}, por escolher analise de dados')
    case 2:
        print(f'Parabéns {nome}, por escolher power bi')
    case 3:
        print(f'Parabéns {nome}, por escolher desenvolvimento de banco de dados')
    case 4:
        print('Acesse nosso site e veja outras opções')
    case _:
        print('Opção inválida')
        
