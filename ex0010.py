largura = float(input('Largura da parede:'))
altura = float(input('Lagura da parede:'))
área = largura * altura
tinta = área / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}.' .format(largura, altura, área))
print('Para pintar esssa parede, você precisará de {}l de tinta.' .format(tinta))