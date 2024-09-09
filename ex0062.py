cont = ('Zero', 'Um', 'Dois', 'Três',
    'Quatro', 'Cinco', 'Seis', 'Sete',
    'Oito', 'Nove', 'Dez')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        print(f'Você digitou o número {cont[num]}')
        resposta = str(input('Quer continuar? [s/n]:'.upper().strip()))
        if resposta[0] in 'Nn':
            break
    else:
        print('Número fora do intervalo. Tente novamente.', end='')