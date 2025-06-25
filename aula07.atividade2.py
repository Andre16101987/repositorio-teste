usuarios_filmes = {'joao':['titanic','avatar','exterminador'],'maria':['cidade dos anjos','uma linda mulher'],'carlos':['matrix','vingadores']}

menu = int(input('1-adicionar filme\n2-remover filmeso\n3-ver filmes de um usuario\n4-ver todos os usuarios\n0-sair\n Escolha uma opção '))

match menu:
    case 1:
       nome_usuario = input('Digite seu nome')
       filmes_novos = input('Digite um filme')
       for nome_usuario in usuarios_filmes.keys():
            usuarios_filmes['values'] = filmes_novos
       if not nome_usuario in usuarios_filmes:
          usuarios_filmes.append(nome_usuario)
          usuarios_filmes.append(filmes_novos)

print(usuarios_filmes)