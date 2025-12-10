for i in range(3):
    s = input('Senha: ')
    if s == 'HG':
        acesso = input('Deseja continuar para saber a media do aluno')
        while acesso == 'sim':
            print('Sistema de notas Escolares')
            nome = input('Nome: ')
            n1 = float(input('Nota1: '))
            n2 = float(input('Nota1: '))
            n3 = float(input('Nota1: '))
            n4 = n1+n2+n3
            n5 = n4/3
            print('A media do aluno', nome, 'é', n5 )
            acesso = input('Deseja verificar outro aluno?')
else:
    print('conta bloqueada')

input('Digite enter para sair:')