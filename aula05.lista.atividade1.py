nomes = []
NomesEscolhidos = input('Digite 5 nomes ')
nomes.append(NomesEscolhidos)
print(nomes)
NomeDeletado = input('Escolha um nome para remover da lista ')

if NomeDeletado in nomes:
    nomes.remove(NomeDeletado)
    print(f"Nome '{NomeDeletado}' removido com sucesso!")
else:
    print(f"O nome '{NomeDeletado}' não está na lista.")