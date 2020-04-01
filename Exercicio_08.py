
'''Escreva um Programa que leia um Valor em metros e Exiba convertido e Centimetros e Milimetros.'''

medida = float(input('Digite um Valor Para Ser Calculado:'))
cm = medida * 100
mm =  medida * 1000
km = medida * 1000
dm = medida * 0,10
dam = medida * 0,1
m = medida * 1000
print('Escreva a Medida {}m Corresponde a {:.0f}cm e {:.0f}mm e {}km e {}dm e {}dam '.format(medida,cm,mm,km,dm,dam))

# Fazer a Correçao .