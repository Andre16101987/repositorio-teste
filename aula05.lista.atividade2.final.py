# Listas vazias
itens = []
precos = []

# Coletar 3 produtos e seus preços
for i in range(3):
    produto = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto '{produto}': R$ "))
    
    itens.append(produto)
    precos.append(preco)

# Mostrar produtos com seus preços
print("\nLista de compras:")
for i in range(3):
    print(f"{itens[i]} - R$ {precos[i]:.2f}")

# Calcular e exibir o total
total = sum(precos)
print(f"\nValor total da compra: R$ {total:.2f}")