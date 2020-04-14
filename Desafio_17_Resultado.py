# coding=utf-8
# Faça um programa que leia o comprimento do cateto ,oposto e do cateto adjunte de um
# triangulo
# retangulo retangulo calcule e mostre o comprimento do hipotenusa.

# Com Calculo Simples 
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento da CatetoAdjunte :'))
hi = (co ** 2 + ca ** 2)** (1/2)
print(' A Hipotenuza vai medir {:.2f}'.format(hi)) 


# Importando Biblioteca Math (hypot)
import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento da CatetoAdjunte :'))
hi = math.hypot(co,ca)
print(' A Hipotenuza vai medir {:.2f}'.format(hi)) 


# Importando Somente a Biblioteca Hypot
from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento da CatetoAdjunte :'))
hi = hypot(co,ca)
print(' A Hipotenuza vai medir {:.2f}'.format(hi)) 