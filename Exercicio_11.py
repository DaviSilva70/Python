'''  Faça um programa que leia a Largura e Altura de uma Parede em Metros ,calcule a sua area ea quantidade de tinta
 que sera necessario para pinta-la cada litro de tinta ,pinta uma area de 2m2. '''


largura = float(input('Dgite a Largura da Parede: '))
altura = float(input('Digite a Altura da Parede:'))
area = largura * altura
print('Sua Parede tem a Dimensao de {} x {} e sua  Area e de {:.2f}M'.format(largura,altura,area))
tinta = area /2
print('Para Pintar esta Area voce Vai Precisar de {:.2f}L'.format(tinta))