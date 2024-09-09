print('{:=^40}'.format('SHOPPING'))
preço = float(input('Qual o preço? R$'))
print(''' FORMAS DE PAGAMENTO 
[ 1 ] À VISTA DINHEIRO
[ 2 ] À VISTA CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opção = int(input('Qual é a forma de pagamento? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 /  100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totparc, parcela))
else:
    total = preço
    print(' \033[1;31mOpção inválida.\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total)) 