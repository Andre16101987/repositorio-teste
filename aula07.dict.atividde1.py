produto = {'nome': 'mouse','preco': 49.90,'estoque': 25}

for a,b in produto.items():
    print(f'{a} : {b}')

escolha = input('Escolha uma chave ')
print(produto.get(escolha))

if not escolha in produto:
    print('Essa informação não está disponível')

produto['categoria'] = 'informatica'
produto['preco'] = 59.90

for a,b in produto.items():
    print(f'{a} : {b}')

del produto['estoque']

for a,b in produto.items():
    print(f'{a} : {b}')
