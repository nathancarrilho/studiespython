peso = float(input('Qual é o seu peso? (KG)'))
altura = float(input('Qual é a sua altura? (M)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('Você está na faixa de PESOA NORMAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
elif 40 >= imc:
    print('Você está em OBESIDADE MÓRBIDA.')