# coding=utf-8
'''Faça um programa que leia uma frase pelo teclado e
 mostre.
* Quantas vezes apareçe a letra A:
* Em que posiçao ela aparece a primeira vez:
* Em que posiçao ela aparece a por ultima vez: '''

frase = str(input('Digite uma Frase : ')).upper().strip()
print('A Letra A Tantas {} vezes\n '.format(frase.count('A')))
print('A Primeira letra A apareceu na posiçao {}\n'.format(frase.find('A')+1))
print('A Ultima letra apareceu na Posiçao {}'.format(frase.rfind('A')+1))