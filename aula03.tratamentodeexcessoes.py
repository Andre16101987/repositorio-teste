try:
    num1 = int(input('Digite um número '))
    num2 = int(input('Digite o segundo número '))
    
    divisão = num1 / num2
    resultado = round(divisão,2)
    print(f'\nA divisão é {resultado}\n')

except ZeroDivisionError:
    print('Divisão por zero não é permitido ')
except ValueError:
    print('Digite um nº válido')
except:
    print('Erro inesperado')