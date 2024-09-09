velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade >80:
    print('MULTADO! Você excedeu o limite permitido que é 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha uma boa viagem e dirija com segurança!')