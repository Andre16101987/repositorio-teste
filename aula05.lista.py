lista = ['João',16,'Santa Cruz']
print(f'O aluno {lista[0]} tem {lista[1]} anos e mora em {lista[2]}')

lista.append('Rio de janeiro')

print(f'O aluno {lista[0]} tem {lista[1]} anos e mora em {lista[2]} e na cidade {lista[3]}')

lista.insert(1,'Masculino')

print(lista)

'''del lista[1] # remove o indice 1
lista.pop(2)
lista.remove()
print(lista[1:4])''' # printa do primeiro ao 3