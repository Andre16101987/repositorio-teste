
while True:
    try:
        num1 = int(input('Digite um úmero '))
        break
    except ValueError:
        print('Digite um número')


while True:
    try:
        opcao = input('Digite o operador (+,-,*,/): ')
        if opcao in ['+','-','*','/']:
            break
        else:
         print('Operação inválida')
    except ValueError:
         print(f'Erro')

while True:
    try:
        num2 = int(input('Digite outro número: '))
        if opcao == '/' and num2 == 0:
            raise ValueError('Não é possível dividir por zero')
        break
    except ValueError as e:
        print(f'Erro: {e}')

if opcao == '+':
    print({num1 + num2})
elif opcao == '-':
    print({num1 - num2})
elif opcao == '*':
     print({num1 * num2})
elif opcao == '/':
    print({num1 / num2})
else:
    print('Digite um operador válido')
          


