notas = []

# Pedir 10 notas ao usuário
for i in range(10):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

# Calcular média, maior e menor nota
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

# Encontrar notas acima da média
acima_da_media = [nota for nota in notas if nota > media]

# Mostrar os resultados
print("\nResultados:")
print(f"Média das notas: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print("Notas acima da média:", acima_da_media)