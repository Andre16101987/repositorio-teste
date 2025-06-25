nomes = []

# Pedir 5 nomes
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)

'''# Mostrar a lista de nomes
print("Lista de nomes:")
for nome in nomes:
    print(nome)

nome_verificar = input("\nDigite um nome para verificar se está na lista: ")
if nome_verificar in nomes:
    print(f"O nome '{nome_verificar}' está na lista.")

# Pedir o nome a ser deletado
nome_para_deletar = input("Digite o nome que você deseja deletar: ")

# Remover o nome, se ele existir na lista
if nome_para_deletar in nomes:
    nomes.remove(nome_para_deletar)
    print(f"O nome '{nome_para_deletar}' foi removido.")
else:
    print("Esse nome não está na lista.")

# Mostrar a lista final
print("Lista atualizada:")
for nome in nomes:
    print(nome)'''