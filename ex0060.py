from random import randint
computador = randint(1, 10)
print('*' * 20)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar?')
print('*' * 20)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {tentativas} tentativas.')