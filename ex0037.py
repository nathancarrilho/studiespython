nome = str(input('Digite seu nome: '))
if nome == 'Walter':
    print('\033[1;32mAcesso permitido!\033[m')
elif nome == 'Saul':
    print('\033[1:32mAcesso permitido!\033[m')
else:
    print('\033[1;31m Acesso negado! \033[m')
print('Have a good day \033[1;34m{}!\033[m'.format(nome))