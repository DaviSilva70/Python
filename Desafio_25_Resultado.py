'''Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva'no nome.'''

nome = str(input('Digite seu Nome Completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
 # print(nome[:5].upper() == "Silva")
