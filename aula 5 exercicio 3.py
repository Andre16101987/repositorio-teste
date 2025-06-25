notas = []

while True:
    try:
        for i in range(1, 11):
            nota = int(input(f'Digite a {i}º nota: '))       
            notas.append(nota)        
        break
    except:
        print('Digite apenas números válidos')

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)
acima_media = [nota for nota in notas if nota > media]

print(f'A média das notas é: {media}, a maior nota é: {maior}, a menor nota é {menor} e a(s) nota(s) acima da média é/são: {acima_media}')