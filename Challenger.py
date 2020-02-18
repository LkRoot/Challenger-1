print('Seja Bem Vindo')
print()
largura = float(input('Informe a Largura da parede: '))
altura = float(input('Informe a Altura da parede: '))
area = largura * altura
print('A dimensão da sua parede é de {}x{} e a sua Area é de {}m² '.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede você devera usar {}L de Tinta'.format(tinta))
print()
print('Desenvolved by \033[1;31;40mLuccas Santana\033[m')
