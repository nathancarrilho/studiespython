salário = float(input('Qual é o salário? £ '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('O salário será reajustado de \033[1;31;40m £{:.2f} \033[m para \033[1;32;40m £{:.2f} \033[m '.format(salário, novo))