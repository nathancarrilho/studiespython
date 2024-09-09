num = int(input('Digite um número inteiro: '))
print('''Escolha umas das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Digite sua opção:'))
if opção == 1:
    print('O valor {} convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif opção == 2:
    print('O valor {} convertido para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif opção == 3:
    print('O valor {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('\033[;33m Opção inválida. Tente novamente. \033[m')