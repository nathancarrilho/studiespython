a = int(input('Digite um número:'))
b = int(input('Digite um número:'))
c = int(input('Digite um número:'))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}{}{}.'.format('\033[4;33;40m', menor, '\033[m'))
print('O maior valor digitado foi {}{}{}.'.format('\033[4;34;40m', maior, '\033[m'))