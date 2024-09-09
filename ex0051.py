num = int(input('Digite um número para ver sua tabuáda: '))
for c in range (1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))