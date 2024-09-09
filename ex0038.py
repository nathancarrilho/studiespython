casa = float(input('Qual é o valor da casa? $'))
salário = float(input('Qual é o seu salário? $'))
anos = int(input('Em quantos anos pretende financiar?'))
prestação = casa / (anos * 12)
mínimo = (salário / 100) * 20
print('Para pagar uma casa de ${:.2f} em {} anos a prestação será de ${:.2f}'.format(casa, anos, prestação))
if prestação >= mínimo:
    print('\033[1;31m Sua proposta foi recusada.\033[m')
else:
    print('\033[1;32m Sua proposta foi aceita.\033[m')
print('\033[1;33m Obrigado por escolher nossos serviços. \033[m')