nomes = []

while True:
    try:
        nome1 = input('Digite o 1º nome: ').strip().title()
        if not nome1.replace(' ', '').isalpha():
            raise ValueError(('Digite um nome válido, sem números.'))
        
        
        nomes.append(nome1)

        nome2 = input('Digite o 2º nome: ').strip().title()
        if not nome2.replace(' ', '').isalpha():
            raise ValueError(('Digite um nome válido, sem números.'))
        
        
        nomes.append(nome2)

        nome3 = input('Digite o 3º nome: ').strip().title()
        if not nome3.replace(' ', '').isalpha():
            raise ValueError(('Digite um nome válido, sem números.'))
        
        
        nomes.append(nome3)

        nome4 = input('Digite o 4º nome: ').strip().title()
        if not nome4.replace(' ', '').isalpha():
            raise ValueError(('Digite um nome válido, sem números.'))
        
        
        nomes.append(nome4)

        nome5 = input('Digite o 5º nome: ').strip().title()
        if not nome5.replace(' ', '').isalpha():
            raise ValueError(('Digite um nome válido, sem números.'))
        
        
        nomes.append(nome5)

        break
    except ValueError as e:
        print(e)


remover = input('Indique um dos nomes pra ser removido: ').strip().title()

print(nomes)
nomes.remove(remover)
print(nomes)
