real = float(input('Quanto dinheiro você tem na carteira? R$:'))
dolar = real / 5.19
euro = real / 5.51
print('Com R${:.2f} você pode comprar US${:.2f} ou £{:.2f}'.format(real, dolar, euro))