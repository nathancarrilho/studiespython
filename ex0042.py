n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
média = (n1 + n2) / 2
print('Tirando a nota {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, média))
if média >= 7:
    print('\033[1;32mVocê está aprovado!\033[m')
elif média >=5 and média <=7 :
    print('\033[1;33mVocê está de recuperação!\033[m')
elif média < 5:
    print('\033[1;31mVocê está reprovado! \033[m')