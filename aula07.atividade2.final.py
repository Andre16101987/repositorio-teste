usuarios_filmes = {'joao':['titanic','avatar','exterminador'],
                   'maria':['cidade dos anjos','uma linda mulher'],
                   'carlos':['matrix','vingadores']}

menu = int(input('1-adicionar filme\n2-remover filmeso\n3-ver filmes de um usuario\n4-ver todos os usuarios\n0-sair\n Escolha uma opção '))

match menu:
    case 1:
      nome_usuario = input('Digite seu nome')
      filmes_novos = input('Digite um filme')
      if nome_usuario in usuarios_filmes:
        usuarios_filmes[nome_usuario].append(filmes_novos)

      if nome_usuario in usuarios_filmes:
        print(f'filmes do usuario {nome_usuario}: {usuarios_filmes[nome_usuario]}')
        print(usuarios_filmes[nome_usuario])

      else:
       print(f'usuario {nome_usuario} não existe')
       verifica = input(f'deseja adicionar o usuario {nome_usuario} e o filme {filmes_novos}\n digite [S] ou [N]: ')
       if verifica.lower() == 's':
        print(f'usuario {nome_usuario} adicionado')
        usuarios_filmes[nome_usuario] = []
        usuarios_filmes[nome_usuario].append(filmes_novos)

    case 2:
        nome_usuario = input('Escolha um usuário')
        filme_tirar = input('Escolha um filme')

        print(usuarios_filmes.get(nome_usuario, 'usuario não existe'))

        if filme_tirar in usuarios_filmes[nome_usuario]:
            usuarios_filmes[nome_usuario].remove(filme_tirar)
        print(f'filme {filme_tirar} foi retirado do usuario {nome_usuario}')

    case 3:
        nome_usuario = input('Digite o usuário')
        print(usuarios_filmes.get(nome_usuario,'usuário não encontrado'))

    case 4:
      for i in usuarios_filmes.keys():
         print(i)

    case 0:
      print('Sair')
      
       
        