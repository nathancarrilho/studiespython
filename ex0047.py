from random import randint
from time import sleep
itens = ('PEDRA' , 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print(''' SUA JOGADA:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?' ))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCE')
    elif jogador == 2:
        print('O COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if computador == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if computador == 2:
    if jogador == 0:
        print('O JOGADOR VENCE')
    elif jogador == 1:
        print('O COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')