produto = float(input('Qual é o preço do produto? R$'))
promoção = produto - (produto * 5 / 100)
print('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.' .format(produto, promoção))