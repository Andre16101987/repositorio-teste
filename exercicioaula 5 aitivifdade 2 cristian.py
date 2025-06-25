itens = []
precos = []

while True:
    try:
        for i in range(1, 4):
            produto = input(f'Digite o {i}º produto: ').strip().title()
            if not produto.replace(' ', '').isalpha():
                raise ValueError('Digite um iten válido, sem números.')
            itens.append(produto)        
        break
    except ValueError as e:
        print(e)
        itens.clear()  # limpa a lista para reiniciar a coleta dos nomes

while True:
    try:
        for i in range(1, 4):
            valor = int(input(f'Digite o {i}º preço: '))
            precos.append(valor)        
        break
    except ValueError:
        print('Digite apenas números')
        itens.clear()  # limpa a lista para reiniciar a coleta dos nomes

print(f' {itens[0]} custa {precos[0]}, {itens[1]} custa {precos[1]}, {itens[2]} custa {precos[2]}')

soma = sum(precos)

print(f'O valor total da compra é {soma}')