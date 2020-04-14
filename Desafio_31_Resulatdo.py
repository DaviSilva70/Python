'''Desenvolva um programa que pergunte a distancia de uma viagem em km Calcule o preço sa passagem ,cobrando
R$ 0.50 por km para viagens de ate 200km a R$ 0.45 para viagens mais longas.'''

# Primeira Forma.
distancia = float(input('Qual foi a Distancia Percorrida em KM:'))
print('Voce esta Prestes a Começau sua Viagem de {} KM '.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:    
    preco = distancia * 0.45
print('Sua Viagem deu R$: {:.2f}'.format(preco))  


# Segunda Forma com if Simplificad. 


distancia = float(input('Qual foi a Distancia Percorrida em KM:'))
print('Voce esta Prestes a Começau sua Viagem de {} KM '.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O Preço da Sua Viagem e de R$:{:.2F}'.format(preco))